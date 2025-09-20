interface Device {
    var isEnabled: Boolean
    var volume: Int
    fun enable()
    fun disable()
    fun setVolume(percent: Int)
}

class TV : Device {
    override var isEnabled = false
    override var volume = 30

    override fun enable() { isEnabled = true; println("TV: enabled") }
    override fun disable() { isEnabled = false; println("TV: disabled") }
    override fun setVolume(percent: Int) {
        volume = percent.coerceIn(0, 100)
        println("TV: volume set to $volume%")
    }
}

class Radio : Device {
    override var isEnabled = false
    override var volume = 10

    override fun enable() { isEnabled = true; println("Radio: enabled") }
    override fun disable() { isEnabled = false; println("Radio: disabled") }
    override fun setVolume(percent: Int) {
        volume = percent.coerceIn(0, 100)
        println("Radio: volume set to $volume%")
    }
}

open class Remote(protected val device: Device) {
    open fun togglePower() {
        if (device.isEnabled) device.disable() else device.enable()
    }

    open fun volumeUp() {
        device.setVolume((device.volume + 10).coerceAtMost(100))
    }

    open fun volumeDown() {
        device.setVolume((device.volume - 10).coerceAtLeast(0))
    }
}

class AdvancedRemote(device: Device) : Remote(device) {
    fun mute() {
        device.setVolume(0)
        println("AdvancedRemote: muted")
    }

    fun setSpecificVolume(v: Int) {
        device.setVolume(v)
        println("AdvancedRemote: set volume to $v%")
    }
}

fun main() {
    val tv = TV()
    val radio = Radio()

    val remoteForTv = Remote(tv)
    val advRemoteForRadio = AdvancedRemote(radio)

    println("-- Using basic remote on TV --")
    remoteForTv.togglePower()
    remoteForTv.volumeUp()
    remoteForTv.volumeUp()

    println("\n-- Using advanced remote on Radio --")
    advRemoteForRadio.togglePower()
    advRemoteForRadio.volumeUp()
    advRemoteForRadio.setSpecificVolume(55)
    advRemoteForRadio.mute()
}
