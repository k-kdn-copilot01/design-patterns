# Builder Design Pattern - Java

This folder contains Java implementations of the Builder pattern with two parts:

- `Structure/`: Minimal, pattern-focused classes (Product, Builder, ConcreteBuilder, Director, Client `Main`)
- `Example/`: Real-world style example (Computer) with multiple concrete builders and a demo `Main`

## 📁 Folder Structure

- `Structure/`
  - `House.java` — Product
  - `HouseBuilder.java` — Builder interface (fluent)
  - `ConcreteHouseBuilder.java` — Concrete builder
  - `Director.java` — Orchestrates build steps
  - `Main.java` — Demo for structure-only
- `Example/`
  - `Computer.java` — Product
  - `ComputerBuilder.java` — Builder interface (fluent)
  - `OfficeComputerBuilder.java` — Concrete builder for office PCs
  - `GamingComputerBuilder.java` — Concrete builder for gaming PCs
  - `ComputerDirector.java` — Orchestrates build steps
  - `Main.java` — Demo for real-world example

## 🎯 What Builder Shows

- Separate complex object construction from its representation
- Same construction process can create different representations (via different builders)
- Fluent API for readable build steps

## 🚀 How to Run

1) Structure demo (basic pattern):
```bash
cd Creational/Builder/Java/Structure
javac *.java
java Main
```

2) Example demo (real-world Computer example):
```bash
cd Creational/Builder/Java/Example
javac ../Structure/*.java *.java
java Main
```

## 📊 Expected Output

### Structure/Main
```
Simple House: House{walls=4, doors=1, windows=2, hasGarage=false, hasSwimmingPool=false, hasGarden=false, roofType='gabled'}
Luxury House: House{walls=6, doors=2, windows=8, hasGarage=true, hasSwimmingPool=true, hasGarden=true, roofType='hipped'}
```

### Example/Main (Computer)
```
Office PC: Computer{cpu='Intel Core i5', ramGb=16, storageGb=512, gpu='Integrated Graphics', powerSupply='500W Bronze', wifiEnabled=true, operatingSystem='Windows 11 Pro'}
Gaming PC: Computer{cpu='AMD Ryzen 7', ramGb=32, storageGb=2000, gpu='NVIDIA RTX 4070', powerSupply='750W Gold', wifiEnabled=true, operatingSystem='Windows 11 Home'}
```
