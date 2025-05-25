# Final_Project_Garage_Managment 🏍️🔧

A Python-based Garage Management System that leverages object-oriented programming to manage motorcycles and services. This project allows adding, updating, deleting, and analyzing various motorcycle types and garage services such as repairs, maintenance, and customizations.

---

## 🚀 Features

- ✅ Add/update/delete motorcycles (5 types: Sport, Cruiser, Dirt, Electric, Touring)
- ✅ Add/update/delete services (Maintenance, Repair, Customization)
- ✅ Save/load garage data to/from text files
- ✅ Automatically detect and remove duplicate services
- ✅ Sort motorcycles by name or by year
- ✅ Generate visual bar plots for:
  - Motorcycle types
  - Service types

---

## 🧠 Object-Oriented Structure

The system is built with two main class hierarchies:

- `Motorcycle` base class with subclasses:
  - `SportsBike`, `Cruiser`, `DirtBike`, `ElectricBike`, `TouringBike`
  
- `Service` base class with subclasses:
  - `Maintenance`, `Repair`, `Customization`

The `Garage` class acts as a container and controller, handling all operations (add, delete, update, plots, save/load, etc.)

---

## 📊 Dependencies

- Python 3.x
- `matplotlib`

Install required libraries with:

```bash
pip install matplotlib
