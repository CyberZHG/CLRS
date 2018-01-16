PGraphics graphics;
float margin_x = 80.0;
float margin_y = 80.0;
float layer_height = 100.0;
float leaf_margin = 40.0;
float begin_x;
float begin_y;

Node[] nodes;
int[] names = new int[] {84, 22, 19, 10, 3, 17, 6, 5, 9};
int[] highlights = new int[] {22};
int[] disabled = new int[] {9};
String save_name = "6.3-2_5.png";

class Node {
  String name;
  float x_pos, y_pos;
  ArrayList<Node> edges = new ArrayList<Node>();
  String type = "default";
  
  void setLocation(float x, float y) {
    x_pos = x;
    y_pos = y;
  }
  
  void setText(String t) {
    name = t;
  }
  
  void addEdge(Node node) {
    edges.add(node);
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
      PFont font = createFont("Arial", 22, true);
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

class HighlightNode extends Node {
  HighlightNode() {
    type = "Highlight";
  }
  
  void displayCircle() {
    graphics.beginDraw();
    graphics.strokeWeight(2);
    graphics.stroke(197, 90, 17);
    graphics.fill(246, 124, 42);
    graphics.ellipse(x_pos, y_pos, 50, 50);
    graphics.endDraw();
  }
}

class DisabledNode extends Node {
  DisabledNode() {
    type = "Disabled";
  }
  
  void displayCircle() {
    graphics.beginDraw();
    graphics.strokeWeight(2);
    graphics.stroke(120, 120, 120);
    graphics.fill(163, 163, 163);
    graphics.ellipse(x_pos, y_pos, 50, 50);
    graphics.endDraw();
  }
}

boolean contains(String[] array, String text) {
  if (array == null) {
    return false;
  }
  for (String s : array) {
    if (s.equals(text)) {
      return true;
    }
  }
  return false;
}

Node[] initBinaryTreeFromArray(String[] names, String[] highlights, String[] disabled) {
  Node[] nodes = new Node[names.length];
  for (int i = 0; i < names.length; ++i) {
    if (contains(highlights, names[i])) {
      nodes[i] = new HighlightNode();
    } else if (contains(disabled, names[i])) {
      nodes[i] = new DisabledNode();
    }
    nodes[i].setText(names[i]);
  }
  for (int i = 0; i < nodes.length; ++i) {
    if (i * 2 + 1 < nodes.length) {
      nodes[i].addEdge(nodes[i * 2 + 1]);
      if (i * 2 + 2 < nodes.length) {
        nodes[i].addEdge(nodes[i * 2 + 2]);
      }
    }
  }
  return nodes;
}

int getTreeHeight(Node node) {
  if (node == null) {
    return 0;
  }
  int maxHeight = 0;
  for (Node nextNode : node.edges) {
    maxHeight = max(maxHeight, getTreeHeight(nextNode));
  }
  return maxHeight + 1;
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
    for (int i = 0; i < 2; ++i) {
      Node nextNode = null;
      if (i < node.edges.size()) {
        nextNode = node.edges.get(i);
      }
      x += initLocations(nextNode, h + 1, idx * 2 + i, maxWidth, maxHeight);
    }
    x *= 0.5;
    node.setLocation(x, y);
  }
  return x;
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  graphics = createGraphics(800, 600, JAVA2D);
  graphics.smooth(8);
  String[] str_names = new String[names.length];
  for (int i = 0; i < names.length; ++i) {
    str_names[i] = str(names[i]);
  }
  String[] str_highlights = new String[highlights.length];
  for (int i = 0; i < highlights.length; ++i) {
    str_highlights[i] = str(highlights[i]);
  }
  String[] str_disabled = new String[disabled.length];
  for (int i = 0; i < disabled.length; ++i) {
    str_disabled[i] = str(disabled[i]);
  }
  nodes = initBinaryTreeFromArray(str_names, str_highlights, str_disabled);
  int treeHeight = getTreeHeight(nodes[0]);
  int treeWidth = int(pow(2, float(treeHeight)));
  margin_y = (600 - (treeHeight - 1) * layer_height) * 0.5;
  margin_x = (800 - (treeWidth - 1) * leaf_margin) * 0.5;
  initLocations(nodes[0], 0, 0, (treeWidth - 1) * leaf_margin, treeHeight - 1);
}

void draw() {
  background(255);
  graphics.beginDraw();
  strokeWeight(2);
  stroke(65, 113, 156);
  for (Node node : nodes) {
    if (node.type == "Disabled") {
      continue;
    }
    for (Node nextNode : node.edges) {
      if (nextNode.type == "Disabled") {
        continue;
      }
      graphics.line(node.x_pos, node.y_pos, nextNode.x_pos, nextNode.y_pos);
    }
  }
  graphics.endDraw();
  for (Node node : nodes) {
    node.display();
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}