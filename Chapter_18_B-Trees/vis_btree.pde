PGraphics graphics;
PFont font;
float margin_x = 160.0;
float margin_y = 80.0;
float layer_height = 140.0;
float leaf_margin = 120.0;
float rect_size = 40.0;
float child_size = 10.0;

float max_x = -1e20f, min_x = 1e20f;

Node[] nodes;
int degree = 2;
String[] vals = new String[] {"K Q", "B F", "M", "T W", "A", "C D E", "H", "L", "N P", "R S", "V", "X Y Z"};
String root = "K Q";
String active = "";
String[][] edges = new String[][] {
  {"K Q", "0", "B F"},
  {"K Q", "1", "M"},
  {"K Q", "2", "T W"},
  {"B F", "0", "A"},
  {"B F", "1", "C D E"},
  {"B F", "2", "H"},
  {"M", "0", "L"},
  {"M", "1", "N P"},
  {"T W", "0", "R S"},
  {"T W", "1", "V"},
  {"T W", "2", "X Y Z"},
};
String save_name = "18.2-1_21.png";

class Node {
  float x_pos, y_pos;
  int n;
  String[] keys;
  Node[] children;
  
  Node(String val) {
    keys = split(val, ' ');
    n = keys.length;
    children = new Node[degree * 2];
  }
  
  void setLocation(float x, float y) {
    x_pos = x;
    y_pos = y;
  }
  
  void setSize(int n) {
    this.n = n;
  }
  
  void setText(int i, String t) {
    keys[i] = t;
  }
  
  void setChild(int i, Node node) {
    children[i] = node;
  }
  
  int getLeftPos() {
    return (int)(x_pos - (rect_size * n + child_size * (n + 1)) / 2);
  }
  
  int getCenter(int i) {
    if (i % 2 == 0) {
      return (int)(getLeftPos() + child_size / 2 + i / 2 * (rect_size + child_size));
    }
    return (int)(getLeftPos() + rect_size / 2 + i / 2 * rect_size + (i / 2 + 1) * child_size);
  }
  
  void display() {
    for (int i = 0; i < n + 1; ++i) {
      graphics.beginDraw();
        graphics.strokeWeight(2);
        graphics.stroke(91, 155, 213);
        graphics.fill(164, 194, 229);
        graphics.rect(getCenter(i * 2) - child_size * 0.5, y_pos - rect_size * 0.5, child_size, rect_size);
      graphics.endDraw();
    }
    for (int i = 0; i < n; ++i) {
      graphics.beginDraw();
        graphics.strokeWeight(2);
        if (keys[i].equals(active)) {
          graphics.stroke(220, 97, 65);
          graphics.fill(220, 97, 65);
        } else {
          graphics.stroke(91, 155, 213);
          graphics.fill(91, 155, 213);
        }
        graphics.rect(getCenter(i * 2 + 1) - rect_size * 0.5, y_pos - rect_size * 0.5, rect_size, rect_size);
      graphics.endDraw();
      graphics.beginDraw();
        graphics.fill(250, 250, 250);
        graphics.textFont(font, 22);
        graphics.textAlign(CENTER);
        graphics.text(keys[i], getCenter(i * 2 + 1), y_pos + 8);
      graphics.endDraw();
    }
  }
}

int getTreeHeight(Node node) {
  if (node == null) {
    return 0;
  }
  int maxHeight = 0;
  for (int i = 0; i < node.n; ++i) {
    maxHeight = max(maxHeight, getTreeHeight(node.children[i]));
  }
  return maxHeight + 1;
}

void initLocations(Node node, int h, float x, float margin, float maxWidth, int maxHeight) {
  if (node == null) {
    return;
  }
  float y = margin_y * 0.8 + layer_height * h;
  node.setLocation(x, y);
  float subMargin = margin / node.n;
  for (int i = 0; i <= node.n; ++i) {
    initLocations(node.children[i], h + 1, x - margin * 0.5 + subMargin * i, margin * 0.35, maxWidth, maxHeight);
  }
}

int indexOf(String[] vals, String val) {
  for (int i = 0; i < vals.length; ++i) {
    if (vals[i].equals(val)) {
      return i;
    }
  }
  return -1;
}

void initNodes() {
  nodes = new Node[vals.length];
  for (int i = 0; i < vals.length; ++i) {
    nodes[i] = new Node(vals[i]);
  }
  for (int i = 0; i < edges.length; ++i) {
    int idx = parseInt(edges[i][1]);
    nodes[indexOf(vals, edges[i][0])].setChild(idx, nodes[indexOf(vals, edges[i][2])]);
  }
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  initNodes();
  int treeHeight = getTreeHeight(nodes[indexOf(vals, root)]);
  int treeWidth = int(pow(degree * 2, float(treeHeight - 1)));
  initLocations(nodes[indexOf(vals, root)], 0, margin_x * 2 + (treeWidth - 1) * leaf_margin * 0.5, (treeWidth - 1) * leaf_margin * 0.5, (treeWidth - 1) * leaf_margin, treeHeight - 1);
  for (int i = 0; i < nodes.length; ++i) {
    if (nodes[i] != null) {
      min_x = min(min_x, nodes[i].x_pos);
      max_x = max(max_x, nodes[i].x_pos);
    }
  }
  graphics = createGraphics(int(max_x - min_x + margin_x * 2), int((treeHeight - 1) * layer_height + margin_y * 2), JAVA2D);
  min_x -= margin_x;
  for (int i = 0; i < nodes.length; ++i) {
    if (nodes[i] != null) {
      nodes[i].x_pos -= min_x;
    }
  }
  font = createFont("Arial", 22, true);
}

void draw() {
  background(255);
  graphics.beginDraw();
    graphics.background(255, 255, 255, 0);
    graphics.fill(252);
    graphics.textFont(font, 18);
    graphics.textAlign(LEFT);
    graphics.text("https://github.com/CyberZHG/", 10, 23);
  graphics.endDraw();
  graphics.beginDraw();
    graphics.stroke(30);
    graphics.strokeWeight(1.5);
    graphics.stroke(91, 155, 213);
    for (Node node : nodes) {
      if (node == null) {
        continue;
      }
      for (int i = 0; i <= node.n; ++i) {
        if (node.children[i] != null) {
          graphics.line(node.getCenter(i * 2), node.y_pos + rect_size * 0.5, node.children[i].x_pos, node.children[i].y_pos - rect_size * 0.5);
        }
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