class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def add_workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Invalid worker, need instance of Worker class.")



class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss:
                self._boss.add_workers.remove(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Invalid boss. Need an instance of Boss class.")

    def __repr__(self):
        return f'Name: {self.name}, Company: {self.company}, Boss: {self.boss.name}'


