<?php

/**
 * Prototype interface
 * Định nghĩa contract cho việc clone objects
 */
interface Prototype
{
    public function clone(): Prototype;
}
