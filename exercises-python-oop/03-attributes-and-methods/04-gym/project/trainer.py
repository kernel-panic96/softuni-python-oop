from project.common import dataclass

Trainer = dataclass({
    'name': str,
}, 'Trainer <{self.id}> {self.name}')
