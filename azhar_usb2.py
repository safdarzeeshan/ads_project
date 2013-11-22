from pyudev import Context, Monitor
import glib
import gobject
import pyudev.glib

context = Context()
monitor = Monitor.from_netlink(context)
monitor.filter_by(subsystem='input')
observer = pyudev.glib.GUDevMonitorObserver(monitor)

def device_event(observer, device):
	print('event {0} on device {1}'.format(device.action, device))

observer.connect('device-added', device_event)
monitor.start()
monitor.enable_receiving()

mainloop = gobject.MainLoop()
mainloop.run()