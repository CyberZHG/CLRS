PGraphics graphics;
PFont font;

int[][] vals = new int[][] {{-1, 0, 1, 1, 2, 2, 3, 3, 4, -1, 6},
                            {1, 2, 4, 6, 8, 9, 10}}; 

String[] names  = new String[] {"B", "C"};
int[] begin = new int[] {1, 0};

String save_name = "8.2-1_12.png";

float node_size = 50;
float upper_size = 45;
float margin_x = 40;
float margin_y = 30;

void display(int row, int idx) {
  float x = margin_x + (idx + 1) * node_size;
  float y = margin_y + upper_size + row * (node_size + upper_size);
  graphics.beginDraw();
    graphics.strokeWeight(2);
    if (vals[row][idx] >= 0) {
      graphics.stroke(65, 113, 156);
      graphics.fill(91, 155, 213);
    } else {
      graphics.stroke(120, 120, 120);
      graphics.fill(165, 165, 165);
    }
    graphics.rect(x + 0.5, y + 0.5, node_size - 1, node_size - 1);
  graphics.endDraw();
  x += node_size * 0.5;
  y += node_size * 0.5 + 8;
  if (vals[row][idx] >= 0) {
    graphics.beginDraw();
      graphics.fill(250, 250, 250);
      graphics.textFont(font, 22);
      graphics.textAlign(CENTER);
      graphics.text(str(vals[row][idx]), x, y);
    graphics.endDraw();
  }
  y = margin_y + upper_size * 0.5 + 16 + row * (node_size + upper_size);
  graphics.beginDraw();
    graphics.fill(0, 0, 0);
    graphics.textFont(font, 22);
    graphics.textAlign(CENTER);
    graphics.text(str(begin[row] + idx), x, y);
  graphics.endDraw();
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  int max_length = 0;
  for (int i = 0; i < vals.length; ++i) {
    max_length = max(max_length, vals[i].length);
  }
  float w = (max_length + 1) * node_size + margin_x * 2;
  float h = node_size + upper_size + margin_y * 2 + (vals.length - 1) * (node_size + upper_size);
  graphics = createGraphics(int(w), int(h), JAVA2D);
  graphics.smooth(8);
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
  for (int i = 0; i < vals.length; ++i) {
    graphics.beginDraw();
      float x = margin_x;
      float y = margin_y + upper_size + i * (node_size + upper_size);
      x += node_size * 0.5;
      y += node_size * 0.5 + 8;
      graphics.fill(10);
      graphics.textFont(font, 22);
      graphics.textAlign(RIGHT);
      graphics.text(names[i], x, y);
    graphics.endDraw();
    for (int j = 0; j < vals[i].length; ++j) {
      display(i, j);
    }
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}