import face_recognition
from tkinter import *
import cv2
import os
import keyboard
root = Tk()
root.geometry("400x400")
root.title("Face Login System")
blue_frame = Frame(root,bd=0, highlightthickness=0, background="blue")
blue_frame.place(relx=0, rely=0, relwidth=.7, relheight=1, anchor="nw")
a=StringVar()
b=IntVar()

empcount=1

def register():
    main=Toplevel(root)
    main.geometry("400x400")
    main.configure(bg="cyan")
    Label(main,text="Enter your name: ").place(relx=0.1,rely=0.15,relwidth=0.25,relheight=0.05)
    Label(main,text="Enter your age: ").place(relx=0.1, rely=0.3,relwidth=0.22,relheight=0.05)
    Entry(main,textvariable=a).place(relx=0.35,rely=0.15)
    Entry(main,textvariable=b).place(relx=0.32,rely=0.3)
    Label(main,text="Click Save Button to Record Facial Data",bg="cyan").place(relx=0.12, rely=0.36)
    def Save():
        global empcount
        name=a.get()
        age=b.get()
        os.mkdir("C:/Users/hp/Documents/Getting Started/Face_Login_System/DATA/{}".format(empcount))
        file=open("C:/Users/hp/Documents/Getting Started/Face_Login_System/DATA/{}/Info.txt".format(empcount),"w")
        file.write("This is the Information File of ")
        file.write(name)
        file.write(". He is ")
        file.write(str(empcount))
        file.write(" employee. He works with us.\nHis age is ")
        file.write(str(age))
        file.write(".")
        file.close()
        cam=cv2.VideoCapture(0)
        #cv2.namedWindow("SS App")
        while True:
            ret,frame=cam.read()
            if ret==False:
                Label(main, text="An error occurred. Please try again").place(relx=0.25,rely=0.2)
                break
            cv2.putText(frame, "Press Enter to Record your Facial Data", (17,25),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
            cv2.putText(frame, "Press 'q' to exit", (17,55),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
            cv2.imshow("test",frame)
            cv2.waitKey(1)
            if keyboard.is_pressed('q'):
                break
            elif cv2.waitKey(1)%256 & 0xFF ==13:
                image="face.png"
                path = "C:/Users/hp/Documents/Getting Started/Face_Login_System/DATA/{}".format(empcount)
                cv2.imwrite(os.path.join(path , image), frame)
                print("SS taken")
                Label(main,text="Face Recorded. Your Employee number is ",bg="cyan").place(relx=0.12, rely=0.4)
                Label(main,text=empcount,bg="cyan").place(relx=0.2,rely=0.44)
        empcount+=1
        cam.release()
        cv2.destroyAllWindows()
    
    Button(main,text="Save",command=Save).place(relx=0.4,rely=0.45)

empnum=IntVar()

def login():
    login_win=Toplevel(root)
    login_win.geometry("400x400")
    login_win.configure(bg="cyan")
    Label(login_win,text="Enter your Employee Number: ").place(relx=0.1,rely=0.15)
    Entry(login_win,textvariable=empnum).place(relx=0.52,rely=0.15)
    def match():
        enum=empnum.get()
        print(enum)
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            if not ret:
                Label(login_win, text="An error occurred. Please try again").place(relx=0.25,rely=0.2)
                break
            cv2.putText(frame, "Press Enter to Record your Facial Data", (17,25),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
            cv2.putText(frame, "Press 'q' to exit", (17,55),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 2)
            cv2.imshow("test",frame)
            cv2.waitKey(1)
            if keyboard.is_pressed('q'):
                break
            elif cv2.waitKey(1)%256 & 0xFF ==13:
                login_image="temp.jpeg"
                path_to_save="C:/Users/hp/Documents/Getting Started/Face_Login_System"
                cv2.imwrite(os.path.join(path_to_save,login_image), frame)
        en_login_image=face_recognition.load_image_file("C:/Users/hp/Documents/Getting Started/Face_Login_System/temp.jpeg")
        en_to_comp=face_recognition.load_image_file("C:/Users/hp/Documents/Getting Started/Face_Login_System/DATA/{}/face.png".format(enum))
        comp1=face_recognition.face_encodings(en_login_image)[0]
        comp2=face_recognition.face_encodings(en_to_comp)[0]
        results=face_recognition.compare_faces([comp1],comp2)
        if results:
            Label(login_win,text="Login Successfull").place(relx=0.25,rely=0.25)
        else:
            Label(root, text="An error occurred").place(relx=0.25,rely=0.25)
        cap.release()
        cv2.destroyAllWindows()
    Button(login_win,text="Verify Face ID: ",command=match).place(relx=0.4,rely=0.3)

def exit():
    root.destroy()

Button(root,text="Login",command=login).place(relx=.75,rely=0.12,relwidth=.2,relheight=0.1)
Button(root,text="Register",command=register).place(relx=0.75,rely=.3, relwidth=0.2,relheight=0.1)
Button(root,text="Exit",command=exit).place(relx=0.75,rely=.48, relwidth=0.2,relheight=0.1)

root.mainloop()