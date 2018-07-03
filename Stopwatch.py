# template for "Stopwatch: The Game"
import simplegui
# define global variables
sec = 0
count =0
score =0
timer_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(sec):
    D = sec%10
    sec = sec/10
    BC = sec%60
    if BC < 10 :
        BC = "0" + str(BC)
    A = sec/60
    time = str(A) +":" + str(BC)+"." +str(D)
    return time

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global timer_running
    timer_running = True


def stop():
    global sec
    global score
    timer.stop()
    if timer_running:
        global count
        timer_running = False
        count = count+1
        sec = int(sec)
        if sec%10 == 0:
            score = score +1

def reset():
    global sec
    global count
    global score
    sec = 0
    count =0
    score =0
    timer_running = False

# define event handler for timer with 0.1 sec interval
def time_handler():
    global sec
    sec = sec+1



# define draw handler
def draw(canvas):
    global sec
    seconds = format(sec)
    canvas.draw_text(seconds,(50,100),36,"White")
    canvas.draw_text(str(score) + "/" + str(count) ,(10,30),36, "Red")

# create frame
frame = simplegui.create_frame("StopWatch",200,200)

# register event handlers
timer = simplegui.create_timer(100,time_handler)

frame.set_draw_handler(draw)
frame.add_button("  Reset  ",reset,50)
frame.add_button(" Start  ",start,50)
frame.add_button("  Stop  ",stop,50)

# start frame
frame.start()


# Please remember to review the grading rubric
