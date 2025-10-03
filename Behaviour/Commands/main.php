<?php 

interface Command {
    public function execute();
    public function undo();
}

class Light {
    public function on() {
        echo "💡 Đèn bật\n";
    }
    public function off() {
        echo "💡 Đèn tắt\n";
    }
}

// 3. Concrete Commands
class LightOnCommand implements Command {
    private $light;
    public function __construct(Light $light) {
        $this->light = $light;
    }
    public function execute() {
        $this->light->on();
    }
    public function undo() {
        $this->light->off();
    }
}

class LightOffCommand implements Command {
    private $light;
    public function __construct(Light $light) {
        $this->light = $light;
    }
    public function execute() {
        $this->light->off();
    }
    public function undo() {
        $this->light->on();
    }
}

class RemoteControl {
    private $commandHistory = [];

    public function submit(Command $command) {
        $command->execute();
        $this->commandHistory[] = $command;
    }

    public function undo() {
        $command = array_pop($this->commandHistory);
        if ($command) {
            $command->undo();
        }
    }
}

$light = new Light();

$lightOn  = new LightOnCommand($light);
$lightOff = new LightOffCommand($light);

$remote = new RemoteControl();

$remote->submit($lightOn);   // bật đèn
$remote->submit($lightOff);  // tắt đèn
$remote->undo();             // undo: bật lại đèn

