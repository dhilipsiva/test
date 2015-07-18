let foo: Int = 1
println("Just printing foo: \(foo)")
print("Just printing text: \(Double(12/47))")

var text: String? = nil
if let optText = text{
    println(text)
}else{
    println("Nothing to print")
}

let implicitConstant = 20
let implicitDouble = 20.0
let explicitDouble: Double = 20.3

var list  = ["one", "two", "three", ""]
print(list[1])

var dict = ["dhilipsiva": "Full Stack", "Subho": "CTO"]
print(dict["dhilipsiva"])

var emptyList = [Int]()
emptyList.append(1)
emptyList.append(4)
println(emptyList)

var emptyDict = Dictionary<String, Float>()
emptyDict["Foo"] = 1.9
println(emptyDict)

for item in list {
    switch item {
    case "two":
        println(2)
        break
    default:
        println("Nevermind")
        break
    }
    if !item.isEmpty{
        println(item)
    }
}

for i in 0..<3 {
    print(i)
}

func greeter(msg: String) -> (String -> String){
    func say(name: String) -> String {
        return "\(msg), \(name)!"
    }
    return say
}
var helloGreeter = greeter("Hello")
println(helloGreeter("dhilipsiva"))

func sum(num1: Int, num2:Int = 10) -> Int{
    return num1 + num2
}
println(sum(10, num2: 30))

class Room {
    var length: Float = 0
    var bredth: Float = 0
    var height: Float = 0
    
    init(length: Float, bredth: Float){
        self.length = length
        self.bredth = bredth
    }
    
    func area ()-> Float {
        return length * bredth
    }
    
    var volume: Float {
        get {
            return length * bredth * height
        }
        set {
            height = newValue / (length * bredth)
        }
    }
}

var room = Room(length: 10.34, bredth:10.45)
println(room.area())
room.volume = 50
println(room.volume)

class BedRoom: Room {
    var color: String = ""
    
    init(length: Float, bredth: Float, color: String) {
        self.color = color;
        super.init(length: length, bredth: bredth)
    }
    
    func whatColor() -> String {
        return color
    }
    
    override func area() -> Float {
        println("overridden area!")
        return super.area()
    }
}
var bedRoom = BedRoom(length: 10.4, bredth: 10.5, color: "Green")
println(bedRoom.area())
println(bedRoom.whatColor())

enum Rank: Int {
    case Ace = 1, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King
}
let ace = Rank.Ace
let aceRawValue = ace.rawValue;

