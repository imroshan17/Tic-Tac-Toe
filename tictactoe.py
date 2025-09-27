import tkinter as tk
import tkinter.messagebox


root = tk.Tk()
root.title("tic-tac-toe")
big_frame = tk.Frame(root)
big_frame.pack(fill = 'both', expand=True)
root.geometry('1280x720')

#button 0,0
bu1 = tk.Button(big_frame, text = ' ',)
bu1.grid(row = 0, column = 0, ipadx=40, ipady=40, sticky='news')
bu1.config(command = lambda: ButtonClick(1))

#button 0,1
bu2 = tk.Button(big_frame, text = ' ')
bu2.grid(row = 0, column = 1, ipadx=40, ipady=40, sticky='news')
bu2.config(command = lambda: ButtonClick(2))

#button 0,2
bu3 = tk.Button(big_frame, text = ' ')
bu3.grid(row = 0, column = 2, ipadx=40, ipady=40, sticky='news')
bu3.config(command = lambda: ButtonClick(3))

#button 1,0
bu4 = tk.Button(big_frame, text = ' ')
bu4.grid(row = 1, column = 0, ipadx=40, ipady=40, sticky='news')
bu4.config(command = lambda: ButtonClick(4))

#button 1,1
bu5 = tk.Button(big_frame, text = ' ')
bu5.grid(row = 1, column = 1, ipadx=40, ipady=40, sticky='news')
bu5.config(command = lambda: ButtonClick(5))

#button 1,2
bu6 = tk.Button(big_frame, text = ' ')
bu6.grid(row = 1, column = 2, ipadx=40, ipady=40, sticky='news')
bu6.config(command = lambda: ButtonClick(6))

#button 2,0
bu7 = tk.Button(big_frame, text = ' ')
bu7.grid(row = 2, column = 0, ipadx=40, ipady=40, sticky='news')
bu7.config(command =lambda: ButtonClick(7))

#button 2,1
bu8 = tk.Button(big_frame, text = ' ')
bu8.grid(row = 2, column = 1, ipadx=40, ipady=40, sticky='news')
bu8.config(command = lambda: ButtonClick(8))

#button 2,2
bu9 = tk.Button(big_frame, text = ' ')
bu9.grid(row = 2, column = 2, ipadx=40, ipady=40, sticky='news')
bu9.config(command = lambda: ButtonClick(9))

#player info
playerturn=tk.Label(big_frame,text="   Player 1 turn!  ")
playerturn.grid(row=3,column=0,sticky='snew',ipadx=40,ipady=40)

playerdetails=tk.Label(big_frame,text="       Player 1 is X   \n       Player 2 is O")
playerdetails.grid(row=3,column=2,sticky='snew',ipadx=40,ipady=40)


#restart
res=tk.Button(big_frame, text=" Restart ")
res.grid(row=3, column=1, ipadx=40, ipady=40, sticky='news')
res.config(command = lambda: restartButton())

a=1
b=0
c=0

'''
a is the turn indicator
b is the number of moves played so far(game stops at 9)
c is the game-over flag
'''

def restartButton():
    global a, b, c
    a=1
    b=0
    c=0

    playerturn['text'] = "   Player 1 turn!   "

    bu1.config(text=' ', state='normal')
    bu2.config(text=' ', state='normal')
    bu3.config(text=' ', state='normal')
    bu4.config(text=' ', state='normal')
    bu5.config(text=' ', state='normal')
    bu6.config(text=' ', state='normal')
    bu7.config(text=' ', state='normal')
    bu8.config(text=' ', state='normal')
    bu9.config(text=' ', state='normal')

#after getting result(win or loss or draw) disable button
def disableButton():
    bu1.config(state='disabled')
    bu2.config(state='disabled')
    bu3.config(state='disabled')
    bu4.config(state='disabled')
    bu5.config(state='disabled')
    bu6.config(state='disabled')
    bu7.config(state='disabled')
    bu8.config(state='disabled')
    bu9.config(state='disabled')

def ButtonClick(id):
    global a, b, c
    #for player 1
    if id==1 and a==1 and bu1['text'] == ' ':
        bu1['text'] = 'X'
        a=0
        b+=1


    if id==2 and a==1 and bu2['text'] ==' ':
        bu2['text'] = 'X'
        a=0
        b+=1

    if id==3 and a==1 and bu3['text'] ==' ':
        bu3['text'] = 'X'
        a=0
        b+=1

    if id==4 and a==1 and bu4['text'] ==' ':
        bu4['text'] = 'X'
        a=0
        b+=1

    if id==5 and a==1 and bu5['text'] ==' ':
        bu5['text'] = 'X'
        a=0
        b+=1

    if id==6 and a==1 and bu6['text'] ==' ':
        bu6['text'] = 'X'
        a=0
        b+=1

    if id==7 and a==1 and bu7['text'] ==' ':
        bu7['text'] = 'X'
        a=0
        b+=1

    if id==8 and a==1 and bu8['text'] ==' ':
        bu8['text'] = 'X'
        a=0
        b+=1

    if id==9 and a==1 and bu9['text'] ==' ':
        bu9['text'] = 'X'
        a=0
        b+=1

    
    #for player 2
    if id==1 and a==0 and bu1['text'] == ' ':
        bu1['text'] = 'O'
        a=1
        b+=1

    if id==2 and a==0 and bu2['text'] ==' ':
        bu2['text'] = 'O'
        a=1
        b+=1

    if id==3 and a==0 and bu3['text'] ==' ':
        bu3['text'] = 'O'
        a=1
        b+=1

    if id==4 and a==0 and bu4['text'] ==' ':
        bu4['text'] = 'O'
        a=1
        b+=1

    if id==5 and a==0 and bu5['text'] ==' ':
        bu5['text'] = 'O'
        a=1
        b+=1

    if id==6 and a==0 and bu6['text'] ==' ':
        bu6['text'] = 'O'
        a=1
        b+=1

    if id==7 and a==0 and bu7['text'] ==' ':
        bu7['text'] = 'O'
        a=1
        b+=1

    if id==8 and a==0 and bu8['text'] ==' ':
        bu8['text'] = 'O'
        a=1
        b+=1

    if id==9 and a==0 and bu9['text'] ==' ':
        bu9['text'] = 'O'
        a=1
        b+=1

    if( bu1['text']=='X' and bu2['text']=='X' and bu3['text']=='X' or
        bu4['text']=='X' and bu5['text']=='X' and bu6['text']=='X' or
        bu7['text']=='X' and bu8['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu4['text']=='X' and bu7['text']=='X' or
        bu2['text']=='X' and bu5['text']=='X' and bu8['text']=='X' or
        bu3['text']=='X' and bu6['text']=='X' and bu9['text']=='X' or
        bu1['text']=='X' and bu5['text']=='X' and bu9['text']=='X' or
        bu3['text']=='X' and bu5['text']=='X' and bu7['text']=='X'):
            disableButton()
            c=1
            tk.messagebox.showinfo("Tic Tac Toe","Winner is player 1")

    elif( bu1['text']=='O' and bu2['text']=='O' and bu3['text']=='O' or
        bu4['text']=='O' and bu5['text']=='O' and bu6['text']=='O' or
        bu7['text']=='O' and bu8['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu4['text']=='O' and bu7['text']=='O' or
        bu2['text']=='O' and bu5['text']=='O' and bu8['text']=='O' or
        bu3['text']=='O' and bu6['text']=='O' and bu9['text']=='O' or
        bu1['text']=='O' and bu5['text']=='O' and bu9['text']=='O' or
        bu3['text']=='O' and bu5['text']=='O' and bu7['text']=='O'):
            disableButton()
            c=1
            tk.messagebox.showinfo("Tic Tac Toe","Winner is player 2")

    elif b==9:
            disableButton()
            c=1
            tk.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    if a==1 and c==0:
        playerturn['text']="   Player 1 turn!   "
    elif a==0 and c==0:
        playerturn['text']="   Player 2 turn!   "

root.mainloop()