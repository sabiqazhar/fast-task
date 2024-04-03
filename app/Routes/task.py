from fastapi import HTTPException, Depends, status, APIRouter, Response
from Model import models
from sqlalchemy.orm import Session, joinedload
from Schemas import task
from database import get_db

router = APIRouter()

@router.get("/")
async def get_all(db: Session = Depends(get_db), limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    data = db.query(models.Task).offset(skip).limit(limit).options(joinedload(models.Task.user)).all()
    if data:
        return {'status': 'ok', 'code': 200, 'result': len(data), 'data': data}
    else:
        return {'status': 'error', 'code': 400, 'message': 'data not found'}
    

@router.get("/{id}")
async def get_id(id: int, db: Session = Depends(get_db)):
    data = db.query(models.Task).filter(models.Task.id == id).options(joinedload(models.Task.user)).first()
    if data:
        return {'status': 'ok', 'code': 200, 'data': data}
    else:
        return {'status': 'error', 'code': 400, 'message': 'data not found'}


@router.post("/")
async def post(payload: task.TaskBaseSchema, db: Session = Depends(get_db)):
    new_task = models.Task(**payload.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {'status': 'ok', 'code': 200, 'message': 'data added'}


@router.patch("/{id}")
async def patch(id: int, payload: task.TaskBaseSchema, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task_note = task_query.first()

    if not task_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No task with this id: {id} found')
    
    update_data = payload.dict(exclude_unset=True)
    task_query.filter(models.Task.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(task_note)
    return {"status": "success", 'code': 200, 'message': 'data updated'}

  
@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    task_query = db.query(models.Task).filter(models.Task.id == id)
    task = task_query.first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No task with this id: {id} found')
    task_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)  