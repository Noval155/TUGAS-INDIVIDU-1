{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 770,
   "id": "c4ad88ba-0311-4b2b-b0f8-8edb61532389",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import face_recognition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 771,
   "id": "a287c2ba-62ed-46a5-ae00-3c7166a7d876",
   "metadata": {},
   "outputs": [],
   "source": [
    "#loading gambar untuk mendeteksi\n",
    "original_image = cv2.imread('images/novalmaskerdanamel.jpeg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 772,
   "id": "094a7b21-f913-417c-bc0b-de1b9ad93fb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#load gambar sampel dan dapatkan 128 penyematan wajah dari mereka\n",
    "noval_image = face_recognition.load_image_file('images/noval.jpeg')\n",
    "noval_face_encodings = face_recognition.face_encodings(noval_image)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 773,
   "id": "12a0674a-64b5-488a-bd6b-482573f5b8b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "amel_image = face_recognition.load_image_file('images/amel.jpeg')\n",
    "amel_face_encodings = face_recognition.face_encodings(amel_image)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 774,
   "id": "ac6622df-d5ca-4b6a-8b02-cbc62e8dce82",
   "metadata": {},
   "outputs": [],
   "source": [
    "#save pengkodean dan label yang sesuai dalam array terpisah dalam urutan yang sama\n",
    "known_face_encodings = [noval_face_encodings, amel_face_encodings]\n",
    "known_face_names = [\"noval (562020120014)\", \"amel (222010120001)\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 775,
   "id": "9d23ed86-0480-4858-b692-e55ca40e5254",
   "metadata": {},
   "outputs": [],
   "source": [
    "#load gambar yang tidak diketahui untuk mengenali wajah di dalamnya\n",
    "image_to_recognize = face_recognition.load_image_file('images/novalmaskerdanamel.jpeg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 776,
   "id": "3a64fddf-d81d-4f3d-ae7d-f9ac1b1d9985",
   "metadata": {},
   "outputs": [],
   "source": [
    "all_face_locations = face_recognition.face_locations(image_to_recognize,model='hog')\n",
    "#detect face encodings for all the faces detected\n",
    "all_face_encodings = face_recognition.face_encodings(image_to_recognize,all_face_locations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 777,
   "id": "18046c62-f15f-46a5-abc9-9f9bead5ab79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 1 no of faces in this image\n"
     ]
    }
   ],
   "source": [
    "print('There are {} no of faces in this image'.format(len(all_face_locations)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 778,
   "id": "0587d40f-05d7-40ec-a584-2f43f80e402a",
   "metadata": {},
   "outputs": [],
   "source": [
    "for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):\n",
    "    #splitting the tuple to get the four position values of current face\n",
    "    top_pos,right_pos,bottom_pos,left_pos = current_face_location"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 779,
   "id": "e13dc251-0b3b-4cda-8daa-64c11fa8a434",
   "metadata": {},
   "outputs": [],
   "source": [
    "  all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 780,
   "id": "55e65c39-c225-413c-a43e-a7cd292e7b6e",
   "metadata": {},
   "outputs": [],
   "source": [
    " name_of_person = 'unknown'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 781,
   "id": "8cc2ab58-c001-4874-b3bd-632eae50ff5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "  if True in all_matches:\n",
    "        first_match_index = all_matches.index(True)\n",
    "        name_of_person = known_face_names[first_match_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 782,
   "id": "6d759780-b135-4728-b4a1-69ab5e082c49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       [[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       [[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]],\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]],\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]]], dtype=uint8)"
      ]
     },
     "execution_count": 782,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "  cv2.rectangle(original_image,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 783,
   "id": "318e3c84-8ea6-4051-84a1-901fb1b7b931",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       [[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       [[236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        [236, 242, 249],\n",
       "        ...,\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177],\n",
       "        [160, 158, 177]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]],\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]],\n",
       "\n",
       "       [[  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        ...,\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0],\n",
       "        [  0,   0,   0]]], dtype=uint8)"
      ]
     },
     "execution_count": 783,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " font = cv2.FONT_HERSHEY_DUPLEX\n",
    " cv2.putText(original_image, name_of_person, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 784,
   "id": "a24567e1-6eb7-4e85-b3ab-eef6dbe517e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 784,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " cv2.imshow(\"Faces Identified\",original_image)\n",
    "cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe047ee6-9c9b-4a40-931c-ee48cb0f7245",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41db6758-4f94-4179-9715-2e2f3e07a126",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
