from typing import Dict, List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    customers: List[Customer]
    trainers: List[Trainer]
    equipment: List[Equipment]
    plans: List[ExercisePlan]
    subscriptions: List[Subscription]

    _customers_by_id: Dict[int, Customer]
    _trainers_by_id: Dict[int, Trainer]
    _equipments_by_id: Dict[int, Equipment]
    _plans_by_id: Dict[int, ExercisePlan]
    _subscriptions_by_id: Dict[int, Subscription]

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

        self._customers_by_id = {}
        self._trainers_by_id = {}
        self._equipments_by_id = {}
        self._plans_by_id = {}
        self._subscriptions_by_id = {}

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)
        self._customers_by_id[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)
        self._trainers_by_id[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)
        self._equipments_by_id[equipment.id] = equipment

    def add_plan(self, plan):
        if plan in self.plans:
            return
        self.plans.append(plan)
        self._plans_by_id[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)
        self._subscriptions_by_id[subscription.id] = subscription

    def subscription_info(self, subscription_id: int):
        sub = self._subscriptions_by_id[subscription_id]

        trainer = self._trainers_by_id[sub.trainer_id]
        customer = self._customers_by_id[sub.customer_id]

        plan = self._plans_by_id[sub.exercise_id]
        equipment = self._equipments_by_id[plan.equipment_id]

        return '\n'.join(map(str, [
            sub,
            customer,
            trainer,
            equipment,
            plan
        ]))
