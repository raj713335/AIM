import os
import json
import cv2
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from fastapi import UploadFile, File
from starlette import status
from config.database import SessionLocal
from ..auth import get_user_info
from schemas.userPayload import userPayload

from ml.segment_object_detection import segment_object_detection

router = APIRouter(
    prefix='/ml',
    tags=['Machine Learning']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/segment_object_detection', status_code=status.HTTP_200_OK)
async def segment_object(file: UploadFile = File()):
    try:
        # if user is None:
        #     raise HTTPException(status_code=401, detail='Authentication Failed')

        host = 'http://localhost:5000'

        print(host)

        data = await file.read()
        file_name = f"{os.path.splitext(file.filename)[0]}{os.path.splitext(file.filename)[1]}"
        # Create a file path with the media folder
        file_path = f"static/dumps/{file_name}"
        # Save the file to the folder
        with open(file_path, "wb") as buffer:
            buffer.write(data)

        predictions = segment_object_detection(file_path)

        print(predictions)

        report = []
        for i, obj in enumerate(predictions):
            imagex = obj['roi']  # grayscale image (array)
            x = obj['x']  # name
            y = obj['y']  # name
            w = obj['w']  # name
            h = obj['h']  # name
            class_name = obj['prediction_class']  # name
            prediction_score = obj['prediction_score']  # probability score

            # save grayscale and image in predict folder
            image = f'{file_name}_roi_{i}.jpg'
            cv2.imwrite(f'./static/predict/{image}', imagex)

            # save report
            report.append([host + "/static/predict/" + image,
                           x,
                           y,
                           w,
                           h,
                           class_name,
                           prediction_score])

        response = {"result": host + "/" + f"static/dumps/data/{file_name}", "report": report}

        return Response(json.dumps(response), media_type="application/json")
    except Exception as err:
        raise HTTPException(status_code=401, detail=err)
