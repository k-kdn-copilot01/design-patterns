<?php

require_once 'DocumentPrototype.php';
require_once 'DocumentSettings.php';
require_once 'DocumentManager.php';

/**
 * Main class để demo Prototype pattern với ví dụ thực tế
 * Tạo và quản lý tài liệu với các template khác nhau
 */
class Main
{
    public static function run(): void
    {
        echo "=== PROTOTYPE PATTERN - REAL WORLD EXAMPLE ===\n\n";

        $documentManager = new DocumentManager();

        self::createTemplates($documentManager);

        echo "1. CREATING DOCUMENTS FROM TEMPLATES\n";
        echo "====================================\n";

        $reportDoc = $documentManager->createDocument("Report");
        if ($reportDoc instanceof DocumentPrototype) {
            echo "Created Report Document:\n";
            echo $reportDoc->getInfo() . "\n\n";
        }

        $letterDoc = $documentManager->createDocument("Letter");
        if ($letterDoc instanceof DocumentPrototype) {
            echo "Created Letter Document:\n";
            echo $letterDoc->getInfo() . "\n\n";
        }

        echo "2. CUSTOMIZING CLONED DOCUMENTS\n";
        echo "==============================\n";

        if ($reportDoc instanceof DocumentPrototype) {
            $reportDoc->setTitle("Monthly Sales Report - January 2024");
            $reportDoc->setContent("This report contains detailed analysis of our sales performance...");
            $reportDoc->getSettings()->setTheme("dark");
            $reportDoc->getSettings()->addTag("urgent");
            $reportDoc->getSettings()->addTag("sales");

            echo "Customized Report Document:\n";
            echo $reportDoc->getInfo() . "\n\n";
        }

        if ($letterDoc instanceof DocumentPrototype) {
            $letterDoc->setTitle("Formal Business Letter");
            $letterDoc->setContent("Dear Sir/Madam,\n\nI am writing to inform you about...");
            $letterDoc->getSettings()->setFontSize(12);
            $letterDoc->getSettings()->addTag("formal");
            $letterDoc->getSettings()->addTag("business");

            echo "Customized Letter Document:\n";
            echo $letterDoc->getInfo() . "\n\n";
        }

        echo "3. CREATING MULTIPLE DOCUMENTS\n";
        echo "=============================\n";

        $multipleReports = $documentManager->createMultipleDocuments("Report", 3);
        echo "Created " . count($multipleReports) . " report documents:\n";
        
        foreach ($multipleReports as $index => $doc) {
            if ($doc instanceof DocumentPrototype) {
                $doc->setTitle("Report #" . ($index + 1));
                echo "Document " . ($index + 1) . ": " . $doc->getTitle() . "\n";
            }
        }

        echo "\n4. DEMONSTRATING INDEPENDENCE OF CLONES\n";
        echo "=====================================\n";

        $doc1 = $documentManager->createDocument("Report");
        $doc2 = $documentManager->createDocument("Report");

        if ($doc1 instanceof DocumentPrototype && $doc2 instanceof DocumentPrototype) {
            $doc1->setTitle("Modified Document 1");
            $doc1->getSettings()->setTheme("light");

            $doc2->setTitle("Modified Document 2");
            $doc2->getSettings()->setTheme("dark");

            echo "Document 1: " . $doc1->getTitle() . " (Theme: " . $doc1->getSettings()->getTheme() . ")\n";
            echo "Document 2: " . $doc2->getTitle() . " (Theme: " . $doc2->getSettings()->getTheme() . ")\n";
            echo "Settings objects are independent: " . (spl_object_id($doc1->getSettings()) !== spl_object_id($doc2->getSettings()) ? "Yes" : "No") . "\n";
        }

        echo "\n5. AVAILABLE TEMPLATES\n";
        echo "====================\n";
        $templates = $documentManager->getAvailableTemplates();
        echo "Available templates: " . implode(", ", $templates) . "\n";

        echo "\n=== DEMO COMPLETED ===\n";
    }

    private static function createTemplates(DocumentManager $manager): void
    {
        $reportSettings = new DocumentSettings("Arial", 11, "default", true, ["report", "business"]);
        $reportMetadata = [
            "author" => "System",
            "created_at" => date("Y-m-d H:i:s"),
            "version" => "1.0",
            "category" => "Business"
        ];
        $reportTemplate = new DocumentPrototype(
            "Report Template",
            "This is a template for business reports. Replace this content with your actual report data.",
            $reportMetadata,
            $reportSettings
        );
        $manager->registerTemplate("Report", $reportTemplate);

        $letterSettings = new DocumentSettings("Times New Roman", 12, "classic", false, ["letter", "formal"]);
        $letterMetadata = [
            "author" => "System",
            "created_at" => date("Y-m-d H:i:s"),
            "version" => "1.0",
            "category" => "Communication"
        ];
        $letterTemplate = new DocumentPrototype(
            "Letter Template",
            "This is a template for formal letters. Replace this content with your actual letter content.",
            $letterMetadata,
            $letterSettings
        );
        $manager->registerTemplate("Letter", $letterTemplate);

        $memoSettings = new DocumentSettings("Calibri", 10, "minimal", true, ["memo", "internal"]);
        $memoMetadata = [
            "author" => "System",
            "created_at" => date("Y-m-d H:i:s"),
            "version" => "1.0",
            "category" => "Internal"
        ];
        $memoTemplate = new DocumentPrototype(
            "Memo Template",
            "This is a template for internal memos. Replace this content with your actual memo content.",
            $memoMetadata,
            $memoSettings
        );
        $manager->registerTemplate("Memo", $memoTemplate);
    }
}

Main::run();
