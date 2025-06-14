{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00d7374b-9b6a-4b6a-b583-a8c75220d44c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      1\n",
      "     1 1\n",
      "    1 2 1\n",
      "   1 3 3 1\n",
      "  1 4 6 4 1\n"
     ]
    }
   ],
   "source": [
    "n = 5\n",
    "\n",
    "for i in range(1, n+1):\n",
    "    for j in range(0, n-i+1):\n",
    "        print(' ', end='')\n",
    "\n",
    "    C = 1\n",
    "\n",
    "    for j in range(1, i+1):\n",
    "\n",
    "        print(' ', C, sep='', end='')\n",
    "\n",
    "        C = C * (i - j) // j\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e82ec07c-6619-40f3-b772-9ee660a67e4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=4\n",
    "c=3*4+5\n",
    "a+=10-2\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c6c4097a-e94b-4140-a577-0bf2db11fb31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "while a<10:\n",
    "    print(a)\n",
    "    a+=2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "771dcdff-8d0f-42ab-9649-184254f8c758",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*\n",
      "**\n",
      "***\n",
      "****\n",
      "*****\n",
      "******\n",
      "*******\n",
      "********\n",
      "*********\n",
      "**********\n"
     ]
    }
   ],
   "source": [
    "n=10\n",
    "for i in range(n):\n",
    "    print('*'* (i+1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e4feb99-1907-43eb-a307-a5c7e7251b33",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for //: 'str' and 'int'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m (n):\n\u001b[0;32m      3\u001b[0m     count\u001b[38;5;241m=\u001b[39mn\u001b[38;5;241m-\u001b[39mi\n\u001b[1;32m----> 4\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m*\u001b[39m count\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m2\u001b[39m)\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m*\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m*\u001b[39m (i\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m))\n",
      "\u001b[1;31mTypeError\u001b[0m: unsupported operand type(s) for //: 'str' and 'int'"
     ]
    }
   ],
   "source": [
    "n=5\n",
    "for i in range (n):\n",
    "    count=n-i\n",
    "    print(''* count//2)\n",
    "    print('*'* (i+1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5d6229e8-2ee4-4f5b-80d4-805f8602a861",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "a=1\n",
    "b=5\n",
    "c=3\n",
    "print(a+b+c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0419015d-0cd7-48ff-829f-f2af5051d596",
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
    "a=int(\"20\",8)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f65870b4-b54e-43ae-91e4-833817b88dce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "53\n"
     ]
    }
   ],
   "source": [
    "a=\"5\"\n",
    "a+=\"3\"\n",
    "t=int(a)+2\n",
    "print(float(t))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "051aecc5-28d7-44e8-a0ff-bd0d05df4b60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ath\n"
     ]
    }
   ],
   "source": [
    "x=\"datha\"\n",
    "print(x[1:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a3314959-c645-4885-9dba-6bff866d69f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    *\n",
      "   ***\n",
      "  *****\n",
      " *******\n",
      "*********\n"
     ]
    }
   ],
   "source": [
    "n=5\n",
    "for i in range(1,n+1):\n",
    "    for spaces in range(1,n-i+1):\n",
    "        print(\" \",end=\"\")\n",
    "    for j in range(1,2*i):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "df812eb6-aa1b-45ae-8956-2f21c62dd69f",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'ab' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[12], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m a\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5\u001b[39m\n\u001b[0;32m      2\u001b[0m b\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m2\u001b[39m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28mprint\u001b[39m(ab\u001b[38;5;241m-\u001b[39m(a\u001b[38;5;241m%\u001b[39mb))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'ab' is not defined"
     ]
    }
   ],
   "source": [
    "a=5\n",
    "b=2\n",
    "print(ab-(a%b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f480007a-a09a-472c-a6e0-6dfe021f3207",
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
