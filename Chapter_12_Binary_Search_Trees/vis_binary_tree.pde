PGraphics graphics;
float margin_x = 80.0;
float margin_y = 80.0;
float layer_height = 100.0;
float leaf_margin = 5.0;

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
  
  void display() {
    displayCircle();
    displayText();
  }
}

int getTreeHeight(Node node) {
  if (node == null) {
    return 0;
  }
  return max(getTreeHeight(node.left), getTreeHeight(node.right)) + 1;
}

float initLocations(Node node, int h, int idx, float maxWidth, int maxHeight) {
  float y = margin_y + layer_height * h;
  float x = 0.0;
  int nodeNum = int(pow(2, float(h)));
  if (h == maxHeight) {
    float div = maxWidth / (nodeNum - 1);
    x = margin_x + div * idx;
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

Node[] nodes;
String save_name = "12.1-1_5.png";
PFont font;

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  nodes = new Node[] {new Node(1), new Node(4), new Node(5), new Node(10), new Node(16), new Node(17), new Node(21)};
  nodes[0].right = nodes[1];
  nodes[1].right = nodes[2];
  nodes[2].right = nodes[3];
  nodes[3].right = nodes[4];
  nodes[4].right = nodes[5];
  nodes[5].right = nodes[6];
  Node root = nodes[0];
  int treeHeight = getTreeHeight(root);
  int treeWidth = int(pow(2, float(treeHeight)));
  graphics = createGraphics(int((treeWidth - 1) * leaf_margin + margin_x * 2), int((treeHeight - 1) * layer_height + margin_y * 2), JAVA2D);
  graphics.smooth(8);
  initLocations(root, 0, 0, (treeWidth - 1) * leaf_margin, treeHeight - 1);
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
    strokeWeight(2);
    stroke(65, 113, 156);
    for (Node node : nodes) {
      if (node.left != null) {
        graphics.line(node.x_pos, node.y_pos, node.left.x_pos, node.left.y_pos);
      }
      if (node.right != null) {
        graphics.line(node.x_pos, node.y_pos, node.right.x_pos, node.right.y_pos);
      }
    }
  graphics.endDraw();
  for (Node node : nodes) {
    node.display();
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}