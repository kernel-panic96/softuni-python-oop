from project.common import dataclass

Customer = dataclass({
    'name': str,
    'address': str,
    'email': str,
}, 'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}')
