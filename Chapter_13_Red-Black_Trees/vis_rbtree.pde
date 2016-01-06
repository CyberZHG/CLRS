PGraphics graphics;
PFont font;
float margin_x = 80.0;
float margin_y = 80.0;
float layer_height = 80.0;
float leaf_margin = 25.0;
float nil_margin = 20.0;

Node[] nodes;
int[] vals = new int[] {41, 38, 31, 12, 19, 8};
int[] reds = new int[] {19, 8};
int root = 38;
int[][] edges = new int[][] {{38, 19},
                             {38, 41},
                             {19, 12},
                             {19, 31},
                             {12, 8}
                            };
String save_name = "13.3-2_11.png";

class Node {
  String name;
  float x_pos, y_pos;
  Node left;
  Node right;
  
  Node(int val) {
    name = str(val);
  }
  
  void setLocation(float x, float y) {
    x_pos = x;
    y_pos = y;
  }
  
  void setText(String t) {
    name = t;
  }
  
  void displayCircle() {
    graphics.beginDraw();
      graphics.strokeWeight(2);
      graphics.stroke(65, 113, 156);
      graphics.fill(91, 155, 213);
      graphics.ellipse(x_pos, y_pos, 50, 50);
    graphics.endDraw();
  }
  
  void displayText() {
    if (name != null) {
      graphics.beginDraw();
        graphics.fill(250, 250, 250);
        graphics.textFont(font, 22);
        graphics.textAlign(CENTER);
        graphics.text(name, x_pos, y_pos + 8);
      graphics.endDraw();
    }
  }
  
  void displayNilSub(float x) {
    float y = y_pos + nil_margin * 2.5;
    graphics.beginDraw();
      graphics.strokeWeight(1);
      graphics.stroke(30);
      graphics.line(x_pos, y_pos, x, y);
    graphics.endDraw();
    graphics.beginDraw();
      graphics.stroke(0);
      graphics.fill(0);
      graphics.rect(x - 15, y - 10, 30, 20, 8, 8, 8, 8);
    graphics.endDraw();
    graphics.beginDraw();
        graphics.fill(250, 250, 250);
        graphics.textFont(font, 12);
        graphics.textAlign(CENTER);
        graphics.text("NIL", x, y + 5);
    graphics.endDraw();
  }
  
  void displayNil() {
    if (left == null) {
      displayNilSub(x_pos - nil_margin);
    }
    if (right == null) {
      displayNilSub(x_pos + nil_margin);
    }
  }
  
  void display() {
    displayNil();
    displayCircle();
    displayText();
  }
}

class RedNode extends Node {
  RedNode(int val) {
    super(val);
  }
  
  void displayCircle() {
    graphics.beginDraw();
      graphics.strokeWeight(0);
      graphics.stroke(237, 28, 36);
      graphics.fill(237, 28, 36);
      graphics.ellipse(x_pos, y_pos, 50, 50);
    graphics.endDraw();
  }
}

class BlackNode extends Node {
  BlackNode(int val) {
    super(val);
  }
  
  void displayCircle() {
    graphics.beginDraw();
      graphics.strokeWeight(0);
      graphics.stroke(0);
      graphics.fill(0);
      graphics.ellipse(x_pos, y_pos, 50, 50);
    graphics.endDraw();
  }
}

int getTreeHeight(Node node) {
  if (node == null) {
    return 0;
  }
  return max(getTreeHeight(node.left), getTreeHeight(node.right)) + 1;
}

float initLocations(Node node, int h, int idx, float maxWidth, int maxHeight) {
  float y = margin_y * 0.8 + layer_height * h;
  float x = 0.0;
  int nodeNum = int(pow(2, float(h)));
  if (h == maxHeight) {
    if (h == 0) {
      x = margin_x + maxWidth * 0.5;
    } else {
      float div = maxWidth / (nodeNum - 1);
      x = margin_x + div * idx;
    }
    if (node != null) {
      node.setLocation(x, y);
    }
  } else {
    if (node == null) {
      x += initLocations(null, h + 1, idx * 2, maxWidth, maxHeight);
      x += initLocations(null, h + 1, idx * 2 + 1, maxWidth, maxHeight);
      x *= 0.5;
    } else {
      x += initLocations(node.left, h + 1, idx * 2, maxWidth, maxHeight);
      x += initLocations(node.right, h + 1, idx * 2 + 1, maxWidth, maxHeight);
      x *= 0.5;
      node.setLocation(x, y);
    }
  }
  return x;
}

int indexOf(int[] vals, int val) {
  for (int i = 0; i < vals.length; ++i) {
    if (vals[i] == val) {
      return i;
    }
  }
  return -1;
}

void initNodes() {
  nodes = new Node[vals.length];
  for (int i = 0; i < vals.length; ++i) {
    if (indexOf(reds, vals[i]) >= 0) {
      nodes[i] = new RedNode(vals[i]);
    } else {
      nodes[i] = new BlackNode(vals[i]);
    }
  }
  for (int i = 0; i < edges.length; ++i) {
    if (edges[i][0] >= edges[i][1]) {
      nodes[indexOf(vals, edges[i][0])].left = nodes[indexOf(vals, edges[i][1])];
    } else {
      nodes[indexOf(vals, edges[i][0])].right = nodes[indexOf(vals, edges[i][1])];
    }
  }
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  initNodes();
  int treeHeight = getTreeHeight(nodes[indexOf(vals, root)]);
  int treeWidth = int(pow(2, float(treeHeight)));
  graphics = createGraphics(int((treeWidth - 1) * leaf_margin + margin_x * 2), int((treeHeight - 1) * layer_height + margin_y * 2), JAVA2D);
  graphics.smooth(8);
  initLocations(nodes[indexOf(vals, root)], 0, 0, (treeWidth - 1) * leaf_margin, treeHeight - 1);
  font = createFont("Arial", 22, true);
}

void draw() {
  background(255);
  graphics.beginDraw();
    graphics.fill(252);
    graphics.textFont(font, 18);
    graphics.textAlign(LEFT);
    graphics.text("https://github.com/CyberZHG/", 10, 23);
  graphics.endDraw();
  graphics.beginDraw();
    graphics.stroke(30);
    for (Node node : nodes) {
      if (node == null) {
        continue;
      }
      if (node.left != null) {
        graphics.line(node.x_pos, node.y_pos, node.left.x_pos, node.left.y_pos);
      }
      if (node.right != null) {
        graphics.line(node.x_pos, node.y_pos, node.right.x_pos, node.right.y_pos);
      }
    }
  graphics.endDraw();
  for (Node node : nodes) {
    if (node == null) {
      continue;
    }
    node.display();
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}