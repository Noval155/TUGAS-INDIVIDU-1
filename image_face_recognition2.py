{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 263,
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
   "execution_count": 264,
   "id": "a287c2ba-62ed-46a5-ae00-3c7166a7d876",
   "metadata": {},
   "outputs": [],
   "source": [
    "original_image = cv2.imread('images/amelsamping.jpeg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 265,
   "id": "094a7b21-f913-417c-bc0b-de1b9ad93fb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "amel_image = face_recognition.load_image_file('images/amel.jpeg')\n",
    "amel_face_encodings = face_recognition.face_encodings(amel_image)[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 266,
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
   "execution_count": 267,
   "id": "ac6622df-d5ca-4b6a-8b02-cbc62e8dce82",
   "metadata": {},
   "outputs": [],
   "source": [
    "known_face_encodings = [modi_face_encodings, trump_face_encodings]\n",
    "known_face_names = [\"amel\", \"amel\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 268,
   "id": "9d23ed86-0480-4858-b692-e55ca40e5254",
   "metadata": {},
   "outputs": [],
   "source": [
    "image_to_recognize = face_recognition.load_image_file('images/amelsamping.jpeg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
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
   "execution_count": 270,
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
   "execution_count": 271,
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
   "execution_count": 272,
   "id": "e13dc251-0b3b-4cda-8daa-64c11fa8a434",
   "metadata": {},
   "outputs": [],
   "source": [
    "  all_matches = face_recognition.compare_faces(known_face_encodings, current_face_encoding)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 273,
   "id": "55e65c39-c225-413c-a43e-a7cd292e7b6e",
   "metadata": {},
   "outputs": [],
   "source": [
    " name_of_person = 'amalia nurharisma (222010120001)'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 274,
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
   "execution_count": 275,
   "id": "6d759780-b135-4728-b4a1-69ab5e082c49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[110, 121, 125],\n",
       "        [168, 179, 183],\n",
       "        [174, 180, 185],\n",
       "        ...,\n",
       "        [ 94,  98, 109],\n",
       "        [135, 139, 150],\n",
       "        [105, 109, 120]],\n",
       "\n",
       "       [[ 90, 101, 105],\n",
       "        [141, 152, 156],\n",
       "        [178, 184, 189],\n",
       "        ...,\n",
       "        [108, 112, 123],\n",
       "        [ 96, 100, 111],\n",
       "        [118, 122, 133]],\n",
       "\n",
       "       [[ 61,  72,  76],\n",
       "        [ 99, 110, 114],\n",
       "        [179, 185, 190],\n",
       "        ...,\n",
       "        [110, 114, 125],\n",
       "        [ 80,  84,  95],\n",
       "        [ 91,  95, 106]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[ 28,  28,  44],\n",
       "        [ 47,  47,  63],\n",
       "        [109, 109, 125],\n",
       "        ...,\n",
       "        [ 23,  32,  36],\n",
       "        [ 23,  32,  36],\n",
       "        [ 23,  32,  36]],\n",
       "\n",
       "       [[ 41,  41,  57],\n",
       "        [ 31,  31,  47],\n",
       "        [ 70,  70,  86],\n",
       "        ...,\n",
       "        [ 22,  30,  37],\n",
       "        [ 26,  34,  41],\n",
       "        [ 24,  32,  39]],\n",
       "\n",
       "       [[ 50,  50,  66],\n",
       "        [ 32,  32,  48],\n",
       "        [ 65,  65,  81],\n",
       "        ...,\n",
       "        [ 24,  31,  40],\n",
       "        [ 28,  35,  44],\n",
       "        [ 36,  41,  50]]], dtype=uint8)"
      ]
     },
     "execution_count": 275,
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
   "execution_count": 276,
   "id": "318e3c84-8ea6-4051-84a1-901fb1b7b931",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[110, 121, 125],\n",
       "        [168, 179, 183],\n",
       "        [174, 180, 185],\n",
       "        ...,\n",
       "        [ 94,  98, 109],\n",
       "        [135, 139, 150],\n",
       "        [105, 109, 120]],\n",
       "\n",
       "       [[ 90, 101, 105],\n",
       "        [141, 152, 156],\n",
       "        [178, 184, 189],\n",
       "        ...,\n",
       "        [108, 112, 123],\n",
       "        [ 96, 100, 111],\n",
       "        [118, 122, 133]],\n",
       "\n",
       "       [[ 61,  72,  76],\n",
       "        [ 99, 110, 114],\n",
       "        [179, 185, 190],\n",
       "        ...,\n",
       "        [110, 114, 125],\n",
       "        [ 80,  84,  95],\n",
       "        [ 91,  95, 106]],\n",
       "\n",
       "       ...,\n",
       "\n",
       "       [[ 28,  28,  44],\n",
       "        [ 47,  47,  63],\n",
       "        [109, 109, 125],\n",
       "        ...,\n",
       "        [ 23,  32,  36],\n",
       "        [ 23,  32,  36],\n",
       "        [ 23,  32,  36]],\n",
       "\n",
       "       [[ 41,  41,  57],\n",
       "        [ 31,  31,  47],\n",
       "        [ 70,  70,  86],\n",
       "        ...,\n",
       "        [ 22,  30,  37],\n",
       "        [ 26,  34,  41],\n",
       "        [ 24,  32,  39]],\n",
       "\n",
       "       [[ 50,  50,  66],\n",
       "        [ 32,  32,  48],\n",
       "        [ 65,  65,  81],\n",
       "        ...,\n",
       "        [ 24,  31,  40],\n",
       "        [ 28,  35,  44],\n",
       "        [ 36,  41,  50]]], dtype=uint8)"
      ]
     },
     "execution_count": 276,
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
   "execution_count": 277,
   "id": "a24567e1-6eb7-4e85-b3ab-eef6dbe517e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 277,
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
