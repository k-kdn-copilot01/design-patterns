<?php

require_once 'Prototype.php';
require_once 'ConcretePrototype.php';
require_once 'DeepConcretePrototype.php';
require_once 'Client.php';

class Main
{
    public static function run(): void
    {
        echo "=== PROTOTYPE PATTERN DEMO ===\n\n";

        $referenceObject = new stdClass();
        $referenceObject->value = "Original Reference";
        
        $originalData = [
            'key1' => 'value1',
            'key2' => $referenceObject,
            'key3' => ['nested' => 'data']
        ];

        echo "1. SHALLOW COPY DEMO\n";
        echo "===================\n";
        
        $original = new ConcretePrototype("Original", $originalData, $referenceObject);
        echo "Original object: " . $original->getName() . "\n";
        echo "Original data: " . json_encode($original->getData()) . "\n";
        echo "Original reference ID: " . spl_object_id($original->getReference()) . "\n\n";

        $shallowClone = $original->clone();
        $shallowClone->setName("Shallow Clone");
        
        $shallowData = $shallowClone->getData();
        $shallowData['key1'] = 'modified_value1';
        $shallowClone->setData($shallowData);
        
        $shallowClone->getReference()->value = "Modified Reference";

        echo "After cloning and modifying:\n";
        echo "Original name: " . $original->getName() . "\n";
        echo "Original data: " . json_encode($original->getData()) . "\n";
        echo "Original reference value: " . $original->getReference()->value . "\n";
        echo "Original reference ID: " . spl_object_id($original->getReference()) . "\n\n";

        echo "Shallow clone name: " . $shallowClone->getName() . "\n";
        echo "Shallow clone data: " . json_encode($shallowClone->getData()) . "\n";
        echo "Shallow clone reference value: " . $shallowClone->getReference()->value . "\n";
        echo "Shallow clone reference ID: " . spl_object_id($shallowClone->getReference()) . "\n\n";

        echo "2. DEEP COPY DEMO\n";
        echo "================\n";

        $deepReferenceObject = new stdClass();
        $deepReferenceObject->value = "Deep Original Reference";
        
        $deepOriginalData = [
            'key1' => 'deep_value1',
            'key2' => $deepReferenceObject,
            'key3' => ['nested' => 'deep_data']
        ];

        $deepOriginal = new DeepConcretePrototype("Deep Original", $deepOriginalData, $deepReferenceObject);
        echo "Deep original object: " . $deepOriginal->getName() . "\n";
        echo "Deep original data: " . json_encode($deepOriginal->getData()) . "\n";
        echo "Deep original reference ID: " . spl_object_id($deepOriginal->getReference()) . "\n\n";

        $deepClone = $deepOriginal->clone();
        $deepClone->setName("Deep Clone");
        
        $deepData = $deepClone->getData();
        $deepData['key1'] = 'modified_deep_value1';
        $deepClone->setData($deepData);
        
        $deepClone->getReference()->value = "Modified Deep Reference";

        echo "After deep cloning and modifying:\n";
        echo "Deep original name: " . $deepOriginal->getName() . "\n";
        echo "Deep original data: " . json_encode($deepOriginal->getData()) . "\n";
        echo "Deep original reference value: " . $deepOriginal->getReference()->value . "\n";
        echo "Deep original reference ID: " . spl_object_id($deepOriginal->getReference()) . "\n\n";

        echo "Deep clone name: " . $deepClone->getName() . "\n";
        echo "Deep clone data: " . json_encode($deepClone->getData()) . "\n";
        echo "Deep clone reference value: " . $deepClone->getReference()->value . "\n";
        echo "Deep clone reference ID: " . spl_object_id($deepClone->getReference()) . "\n\n";

        echo "3. CLIENT USAGE DEMO\n";
        echo "===================\n";

        $client = new Client($original);
        $clones = $client->createMultipleClones(3);

        echo "Created " . count($clones) . " clones using Client:\n";
        foreach ($clones as $index => $clone) {
            echo "Clone " . ($index + 1) . ": " . $clone->getName() . "\n";
        }

        echo "\n=== DEMO COMPLETED ===\n";
    }
}

Main::run();
