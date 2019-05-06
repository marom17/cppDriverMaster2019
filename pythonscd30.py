import sys
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

filename = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + " scd30.csv"

class NewDataSCD(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.lastData = "init"
        
    def on_modified(self, event):
        if event.is_directory == False:
            if("scd30" in event.src_path):
                try:
                    f = open(event.src_path)
                    newData = f.read()
                    f.close()
                    if(self.lastData not in newData):
                        now = datetime.now()
                        date_time = now.strftime("%Y-%m-%d %H-%M-%S")
                        data = newData.split(",")
                        txt = date_time + "," + data[1] + "," + data[2] + "," + data[3]
                        print(txt)
                        f = open(filename,"a")
                        f.write(txt)
                        f.close()
                        self.lastData = newData
                    
                except Exception as e:
                    print(e)
                    pass

if __name__ == "__main__":
    f = open(filename,"a")
    f.write("Time,#CO2,#Hum,#Temp")
    f.close()
    event_handler = NewDataSCD()
    observer = Observer()
    observer.schedule(event_handler, path='/var/local', recursive=False)
    observer.start()

    #running loop
    while(True):
        time.sleep(0.5)