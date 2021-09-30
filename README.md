# Traffic Signs Classification

<img src="https://github.com/theS-K-B/dumpyard/blob/e6cfb1d363ff84e8eb8b4486a62a87a441003c05/CheeryShoddyAmurratsnake-size_restricted.gif" width="1000px" height="400px">

---

There are several different types of traffic signs like speed limits, no entry, traffic signals, turn left or right, children crossing, no passing of heavy vehicles, etc. Traffic signs classification is the process of identifying which class a traffic sign belongs to. In this Python project example, we will build a deep neural network model that can classify traffic signs present in the image into different categories. With this model, we are able to read and understand traffic signs which are a very important task for all autonomous vehicles. 

We accessed dataset of our project from [GTSRB - German Traffic Sign Recognition Benchmark](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign). Our "train" foLder contains 43 folders each representing a different class. The range of the folder is from 0 to 42. With the help of the OS module, we iterate over all the classes and append images and their respective labels in the data and labels list.

---

