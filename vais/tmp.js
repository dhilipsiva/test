var openPtr = Module.findExportByName("libc.so", "open");
var argsOfOpen = ['pointer', 'int']
var open = new NativeFunction(openPtr, 'int', argsOfOpen);
vay newOpen = function(pathPtr, flags) {
	var path = Memory.readUtf8String(pathPtr);
	log("Opening '" + path + "'");
	var fd = open(pathPtr, flags);
	log("Got fd: " + fd);
	return fd;
}
var newNativeOpen = new NativeCallback(newOpen, 'int', argsOfOpen);
Interceptor.replace(openPtr, newNativeOpen);
