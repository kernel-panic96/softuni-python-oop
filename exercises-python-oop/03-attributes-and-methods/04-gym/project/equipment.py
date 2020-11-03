from project.common import dataclass

Equipment = dataclass({
    'name': str
}, 'Equipment <{self.id}> {self.name}')
