<?php 

interface Video {
    public function play();
}

class RealVideo implements Video {
    private $filename;

    public function __construct(string $filename) {
        $this->filename = $filename;
        $this->loadFromServer();
    }

    private function loadFromServer() {
        echo "Đang tải video '{$this->filename}' từ server...\n";
    }

    public function play() {
        echo "Phát video '{$this->filename}'\n";
    }
}

class ProxyVideo implements Video {
    private $filename;
    private $realVideo = null;

    public function __construct(string $filename) {
        $this->filename = $filename;
    }

    public function play() {
        if ($this->realVideo === null) {
            // chỉ tạo RealVideo khi cần
            $this->realVideo = new RealVideo($this->filename);
        }
        $this->realVideo->play();
    }
}

$video1 = new ProxyVideo("movie.mp4");
$video2 = new ProxyVideo("music_video.mp4");

echo "Chưa phát video, chưa load file...\n";

$video1->play(); 
$video1->play(); 
$video2->play();

