{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39f3a856-8832-4ecd-8549-f50a3daca856",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "# break statement\n",
    "i=0\n",
    "while (i<10):\n",
    "    print(i)\n",
    "    i=i+1\n",
    "    if i==6:\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "50157915-5507-4837-b9d4-2e8bc756ad4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "i=0\n",
    "while(i<10):\n",
    "    i=i+1\n",
    "    print(i)\n",
    "    if i==8:\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84303d09-7be8-41a7-ad04-e2f8323da6e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[19, 20, 55, 22, 33, 44, 30, 10]\n"
     ]
    }
   ],
   "source": [
    "#swap 2 numbers using tem\n",
    "list=[19,20,30,22,33,44,55,10]\n",
    "i,j= 2, 6\n",
    "tem=list[i]\n",
    "list[i]=list[j]\n",
    "list[j]=tem\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4324271c-365b-4d48-a5d1-9cfdb251e012",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "#p1\n",
    "a=5\n",
    "b=2\n",
    "c=5*2+3\n",
    "a+=13-2\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31cc4fa8-642f-46ed-8f4c-f5676f024686",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "#p3\n",
    "i=1\n",
    "while i<=5:\n",
    "    i=i+1\n",
    "print(i)    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db746130-ae61-4b76-bee4-9d933238ea0a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
