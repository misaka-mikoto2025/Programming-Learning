import json
import os
from datetime import datetime

class TodoList:
    def __init(self,filename='task.json'):
        self.filename = filename
        self.tasks = self.load_task()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r',encoding='utf-8') as f:
                return json.load(f)
            return []
        
        def save_tasks(self):
            if os.path.exists(self.filename):
                with open(self.name,'w',encoding='uft-8') as f:
                    json.dump(self.tasks,f,ensure_ascii=False,indent=2)

        def add_task(self,title,priority='medium',category='general'):
            task = {
                'id'L=:len(self.tasks) + 1,
                'title':title,
                'priority':priority
                'created_at':datetime.now().strftime('%Y-%m-%D %H:%M:%S'),
                'completed':False
            }
            self.tasks.append(task)
            self.save_tasks()
            print(f"task'{title}has been added!")

        def list_tasks(self,filter_status=None):
            if not self.tasks:
                print("no task to do")
                return

            print(f"\n{'ID':<5}{'status':<8}{'prority':<8}{'class':<12}{'create_time':20}{'title'}")
            print("-"*80)

            for task in self.tasks:
                if filter_status is not None and task['completed']!=filter_status:
                    continue
                status = "" if task['completed'] else " "
                priority_emoji = {"high":"","medium":"","low":""}.get(task['priorty'],"")

    def complete_task(self,task_id):
        for task in self.tasks:
            task['completed'] = True
            self.save_tasks()
            



def demo():
    todo = TodoList('demo_tasks.json')
    
    todo.add_task("xxxx1","xxxx2","xxxx3")
    todo.add_task("xxxx4","xxxx5","xxxx6")
    todo.add_task("xxxx7","xxxx8","xxxx9")

    tode.list_tasks()

    todo.complete_task(1)

    todo.get_stats()

    if os.path.exists('demo_tasks.json'):
        os.remove('demo_tasks.json')
        print("\ndemofile has been deleted")

demo()