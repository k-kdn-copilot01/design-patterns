<?php 

// Factory Method
interface Shape{
  public function draw();
}

class Circle implements Shape{
  public function draw(){
    echo "Drawing a Circle".PHP_EOL;
  }
}

class Square implements Shape{
  public function draw(){
    echo "Drawing a Square".PHP_EOL;
  }
}

class ShapeFactory{
  public static function createShape($type){
    switch(strtolower($type)){
      case 'circle':
        return new Circle();
      case 'square':
        return new Square();
      default:
        throw new Exception("Shape type not recognized.");
    }
  }
}

try {
    $shape1 = ShapeFactory::createShape('circle');
    $shape1->draw();

    $shape2 = ShapeFactory::createShape('square');
    $shape2->draw();

} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

?>