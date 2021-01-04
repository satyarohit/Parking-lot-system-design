'''
@author: Satya Prakash
IDE: python spyder
This is a test file to test each method created in the parking_lot_system module

''''

import unittest as ut
#from parking_lot_system import *
from parking_lot_system import Parking_lot,Car,Bike,Suv,Levels,Slots,Vehicle

class Testparksystem(ut.TestCase):
  def test_park(self):
    #print("Under Park_test")
    park = Parking_lot(6,30)
    ans1 = park.park_vehicle(Bike(10,"Airtel"))
    ans2 = park.park_vehicle(Car(20,"Accenture"))
    ans3 = park.park_vehicle(Suv(30,"Google"))

    self.assertEqual(ans1, True)
    self.assertEqual(ans2, True)
    self.assertEqual(ans3, True)


  def test_leave_operation(self):
    #print("Leave operation")
    park = Parking_lot(6, 30)
    ans1 = park.park_vehicle(Suv(20, "Airtel"))
    ans2 = park.Leave_Operation(Suv(20, "Airtel"))
    ans3 = park.Leave_Operation(Suv(20, "Airtel"))

    self.assertTrue(ans1)
    self.assertTrue(ans2)
    self.assertEqual(ans3, None)

  def test_company_parked(self):
    #print("company Park_test")
    park = Parking_lot(6, 30)
    self.assertTrue(park.park_vehicle(Suv(20, "Airtel")))

    self.assertEqual(park.company_Parked("Airtel"), [Suv(20, "Airtel")])
    print(park.company_Parked("Airtel"))#prints all the vehicle parked with company name given "Airtel"

  def test_complete(self):
    park = Parking_lot(3, 10)
        
    self.assertTrue(park.park_vehicle(Bike(10, "Airtel")))#parking one bike 
        
    self.assertEqual(park.company_Parked("Airtel"), [Bike(10, "Airtel")])#should return one bike we parked above.
        
    self.assertTrue(park.Leave_Operation(Bike(10, "Airtel")))# Remove bike.
        
    self.assertEqual(park.company_Parked("Airtel"), [])#returns empty as no car parked

if __name__ == "__main__":
  ut.main()

