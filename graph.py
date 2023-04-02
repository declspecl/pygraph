class GraphObject:
    def to_string(self):
        return "graph object"

class Point2D(GraphObject):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_string(self) -> str:
        return f"({self.x}, {self.y})"

# class Point3D(Point2D):
#     def __init__(self, x: float, y: float, z: float):
#         super(x, y)
        
#         self.z = z

# inheritence vs aggregation

class CornerPoints(GraphObject):
    def __init__(self, tl: Point2D, tr: Point2D, br: Point2D, bl: Point2D):
        self.tl = tl
        self.tr = tr
        self.br = br
        self.bl = bl

    def to_string(self) -> str:
        return "tl: {}, tr: {}, br: {}, bl: {}".format(self.tl.to_string(), self.tr.to_string(), self.br.to_string(), self.bl.to_string())

class Square(GraphObject):
    def __init__(self, sideLength: float, centerPoint: Point2D):
        self.sideLength = sideLength
        self.centerPoint = centerPoint

    def area(self) -> float:
        return self.sideLength ** 2

    def find_corner_points(self) -> CornerPoints:
        # 0,0 sideLength = 2 -> -1,1 1,-1, 1,1 -1,-1

        half_length: float = self.sideLength / 2
        
        return CornerPoints(
            Point2D(self.centerPoint.x - half_length, self.centerPoint.y + half_length), # tl
            Point2D(self.centerPoint.x + half_length, self.centerPoint.y + half_length), # tr
            Point2D(self.centerPoint.x + half_length, self.centerPoint.y - half_length), # br
            Point2D(self.centerPoint.x - half_length, self.centerPoint.y - half_length)  # bl
        )
 
    def is_point_in_square_using_corners(self, point: Point2D) -> bool:
        cornerPoints: CornerPoints = self.find_corner_points()
        
        return (point.y >= cornerPoints.bl.y and point.y <= cornerPoints.tl.y) and (point.x >= cornerPoints.bl.x and point.x <= cornerPoints.br.x)
    
    def is_point_in_square(self, point: Point2D) -> bool:
        return (point.y >= (self.centerPoint.y - (self.sideLength / 2)) and point.y <= (self.centerPoint.y + (self.sideLength / 2))) and (point.x >= (self.centerPoint.x - (self.sideLength / 2)) and point.x <= (self.centerPoint.x + (self.sideLength / 2)))

    def to_string(self) -> str:
        return "center: {}, side length: {}".format(self.centerPoint.to_string(), self.sideLength)

class Graph(Square):
    def __init__(self, sideLength: float, centerPoint: Point2D, objects: list[GraphObject] = []):
        self.sideLength = sideLength
        self.centerPoint = centerPoint
        self.objects = objects

    # want to be able to add: point, Square
    def add_object(self, object: GraphObject):
        self.objects.append(object)

    def draw(self) -> str:
        # should be a 2d array of characters
        grid: str = "\n".join(["".join(["-" for row in range(self.sideLength)]) for col in range(self.sideLength)])
        gridCopy = []
        storage = []
        newGrid = ""
        i = 0 
        for point in grid:
            i += 1
            if point == '\n':
                i -= 1
                continue
            storage.append(point)
            
            if (i + 1) % self.sideLength == 0:
                gridCopy.append(storage)
                storage = []
        
        gridCopy[0] += '-'

        for object in self.objects:
            if isinstance(object, Point2D):
                # remember, 2d arrays do not exactly work like a coordinate point. the first index is row, not col
                
                # needs to be a 2d array in order to index it. however, its a string rn, and indexing the string wil suck cuz u need to take
                # into account the newlines, so prob cant do len(grid) * object.y math etc.
                
              #bro im just gonna hardcode this because my brain wasnt working

                if object.x == 0 and object.y == 0:
                    gridCopy[self.sideLength - 1][0] = '*'

                elif object.x == self.sideLength and object.y == 0:
                    gridCopy[self.sideLength - 1][self.sideLength - 1] = "*"

                elif object.x == 0 and object.y == self.sideLength:
                    gridCopy[0][0] = '*'
                    
                elif object.x == self.sideLength and object.y == self.sideLength:
                    gridCopy[0][self.sideLength - 1] = '*'

                elif object.x == 0:
                    gridCopy[self.sideLength - object.y - 1][0] = '*'
                
                elif object.y == 0:
                    gridCopy[self.sideLength - object.y - 1][object.x] = '*'

                else:
                    gridCopy[self.sideLength - object.y - 1][object.x - 1] = "*"

            else:
                pass

        # need to be able to represent it as string
        #print(grid)
        for i in gridCopy:
            for j in i:
                
                newGrid += j
       
            newGrid += '\n'
        
        return newGrid


        # need to be able to represent it as string
        return grid

    def to_string(self):
        return ", ".join([object.to_string() for object in self.objects])

graph = Graph(20, Point2D(0, 0))

graph.add_object(Point2D(0, 0))
print(graph.to_string())
print(graph.draw())