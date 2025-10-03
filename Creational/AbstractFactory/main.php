<?php 

// Abstract Factory
interface Button {
    public function render();
}

interface Checkbox {
    public function render();
}

class WinButton implements Button {
    public function render() {
        echo "Rendering Windows Button".PHP_EOL;
    }
}


class MacButton implements Button {
    public function render() {
        echo "Rendering Mac Button".PHP_EOL;
    }
}

class WinCheckbox implements Checkbox {
    public function render() {
        echo "Rendering Windows Checkbox".PHP_EOL;
    }
}

class MacCheckbox implements Checkbox {
    public function render() {
        echo "Rendering Mac Checkbox".PHP_EOL;
    }
}

interface GUIFactory {
    public function createButton(): Button;
    public function createCheckbox(): Checkbox;
}

class WinFactory implements GUIFactory {
    public function createButton(): Button {
        return new WinButton();
    }

    public function createCheckbox(): Checkbox {
        return new WinCheckbox();
    }
}

class MacFactory implements GUIFactory {
    public function createButton(): Button {
        return new MacButton();
    }

    public function createCheckbox(): Checkbox {
        return new MacCheckbox();
    }
}

function getFactory($osType): GUIFactory {
    switch (strtolower($osType)) {
        case 'windows':
            return new WinFactory();
        case 'mac':
            return new MacFactory();
        default:
            throw new Exception("Unknown OS type.");
    }
}

try {
    $osType = 'windows'; // Change to 'mac' to test MacFactory
    $factory = getFactory($osType);

    $button = $factory->createButton();
    $checkbox = $factory->createCheckbox();

    $button->render();
    $checkbox->render();
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
?>