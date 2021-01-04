'''
@author: Satya Prakash
IDE: python spyder
This is a main module which contains various classes and modules.

''''
from enum import Enum
import random
#I have taken only three types of vehicle more can be added here easily!!
class VehicleType(Enum):
  bike = 1
  car = 2
  suv = 3

#vehicle class to instantiate and get type
class Vehicle:
  def __init__(self,plate,company_name,vehicle_type):
    self.plate = plate
    self.company_name = company_name
    self.vehicle_type = vehicle_type
    
  def get_type(self):
    return self.vehicle_type

  #check equal function if details matches or not
  def __eq__(self,other):
    if other is None:
      return False;
    if self.plate != other.plate:
      return False
    if self.company_name != other.company_name:
      return False
    if self.vehicle_type != other.vehicle_type:
      return False
    return True

""" * Bike class( Small vehicle)
 * Car class ( medium vehicle)
 * Suv class ( Large Vehicle)
 * Slot class to park, remove, getvehicle
"""

class Bike(Vehicle):
  def __init__(self,plate,company_name):
    Vehicle.__init__(self,plate, company_name, VehicleType.bike)

class Car(Vehicle):
  def __init__(self,plate,company_name):
    Vehicle.__init__(self,plate, company_name, VehicleType.car)

class Suv(Vehicle):
  def __init__(self,plate,company_name):
    Vehicle.__init__(self,plate, company_name, VehicleType.suv)

class Slots:
  def __init__(self, lane ,spot_number, vehicle_type):
    self.lane = lane
    self.spot_number = spot_number
    self.vehicle = None
    self.vehicle_type = vehicle_type
    
  def isavailable(self):
    return self.vehicle == None
    
  def park(self, vehicle):
    if vehicle.vehicle_type == self.vehicle_type:
      self.vehicle = vehicle
      return True
    else:
      return False

  def remove_vehicle(self):
    self.vehicle = None
    return self.vehicle

  def get_vehicle(self):
    return self.vehicle

"""**Level class with various function**
* park
* remove
* company_name
"""

class Levels:
  def __init__(self, floor, number_of_slots):
    self.floor = floor
    self.slots_in_lane = 10
    self.lanes = number_of_slots / self.slots_in_lane
    self.parking_slots = set()
    self.available_spot = []

    #checking available spot in the lane
    for lane in range(int(self.lanes)):
      for i in range(self.slots_in_lane):
        #random assignment any vehicle type to each slot
        self.available_spot.append(Slots(lane, i ,random.choice(list(VehicleType))))
  
  def park(self,vehicle):
    for slot in self.available_spot:
      if slot.park(vehicle):
        return True
    return False
  
  def remove(self, vehicle):#to detach vehicle from any slot
    for spot in self.available_spot:
      if spot.get_vehicle() == vehicle:
        spot.remove_vehicle()
        return True
    return False
  
  def company_Parked(self,company_name):
    all = [] #to store the vehicles
    for spot in self.available_spot:
      vehicle = spot.get_vehicle()

      if (vehicle is not None) and (vehicle.company_name == company_name):
        all.append(vehicle)
        
    return all

"""**Parking_lot**

* park vehicle 
* Leave operation
* comapny parked
"""

class Parking_lot:
  def __init__(self, number_of_floor, number_of_slot):
    self.levels = []
    for nf in range(number_of_floor):
      self.levels.append(Levels(nf, number_of_slot))

  #Inserts a vehicle into slots 
  def park_vehicle(self, vehicle):
    for lev in self.levels:
      if lev.park(vehicle):
        return True
    return False

  #Exits a vehicle "C" in a level "m"
  def Leave_Operation(self, vehicle):
    for lev in self.levels:
      if lev.remove(vehicle):
        return True
  
  #view the list of vehicle parked of a company
  def company_Parked(self, company_name):
    all = []
    for lev in self.levels:
      all.extend(lev.company_Parked(company_name))
    return all