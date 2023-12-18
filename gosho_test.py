class Worker:
    #part 1 constructor
    def __init__(self, worker_num, fname, lname, worker_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.worker_experience_company = worker_experience_company
        self.salary = salary
        self.age = age

    #part 2 method
    def worker_information(self):
        return f"{self.worker_num}, {self.fname}, {self.lname}, {self.worker_experience_company}, {self.salary}, {self.age}"

    #part 3 new methods
    def salary_bonus(self):
        bonus = 0
        if 5 <= self.worker_experience_company <= 10:
            bonus = self.salary * 0.015
        elif self.worker_experience_company > 10:
            bonus = self.salary * 0.02


        return bonus


def search_by_number(workers_list, number):
    for worker in workers_list:
        if worker.worker_num == number:
            return True

    return False

def search_by_name_experience(workers_list, name, work_experience_company):
    workers_filtered = []
    for worker in workers_list:
        if worker.first_name == name and worker.worker_experience_company == work_experience_company:
            workers_filtered.append(worker)

    return workers_filtered

def add_worker():
    worker_num = input('Enter worker number: ')
    fname = input('Enter worker fname: ')
    lname = input('Enter worker lname: ')
    worker_ep_c = int(input('Enter worker experience in company: '))
    salary = int(input('Enter salary: '))
    age = int(input('Enter age: '))

    workers_list.append(Worker(worker_num, fname, lname, worker_ep_c, salary, age))
def remove_workers(worker_num):
    my_worker = None
    for worker in workers_list:
        if worker.worker_num == worker_num:
            my_worker = worker

    if my_worker is not None:
        workers_list.remove(my_worker)

        print('Informaton deleted!!!')
    else:
        print('Invalid number')


workers_list = []
num_workers = int(input("Enter the number of workers: "))

for _ in range(num_workers):
    
    worker_num = input('Enter worker number: ')
    fname = input('Enter worker fname: ')
    lname = input('Enter worker lname: ')
    worker_ep_c = int(input('Enter worker experience in company: '))
    salary = int(input('Enter salary: '))
    age = int(input('Enter age: '))

    workers_list.append(Worker(worker_num, fname, lname, worker_ep_c, salary, age))
