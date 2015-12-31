PGraphics graphics;
PFont font;

int[] values  = new int[] {-1, -1, 3, 8, -1, -1};
String save_name = "10.1-3_6.png";

float node_size = 50;
float upper_size = 35;
float margin_x = 40;
float margin_y = 30;

void display(int idx) {
  float x = margin_x + idx * node_size;
  float y = margin_y + upper_size;
  graphics.beginDraw();
    graphics.strokeWeight(2);
    if (values[idx] == -1) {
      graphics.stroke(120, 120, 120);
      graphics.fill(165, 165, 165);
    } else {
      graphics.stroke(65, 113, 156);
      graphics.fill(91, 155, 213);
    }
    graphics.rect(x + 0.5, y + 0.5, node_size - 1, node_size - 1);
  graphics.endDraw();
  x += node_size * 0.5;
  y += node_size * 0.5 + 8;
  if (values[idx] != -1) {
    graphics.beginDraw();
      graphics.fill(250, 250, 250);
      graphics.textFont(font, 22);
      graphics.textAlign(CENTER);
      graphics.text(str(values[idx]), x, y);
    graphics.endDraw();
  }
  y = margin_y + upper_size * 0.5 + 8;
  if (values[idx] != -1 && values[(idx + values.length - 1) % values.length] == -1) {
    graphics.beginDraw();
      graphics.fill(0, 0, 0);
      graphics.textFont(font, 22);
      graphics.textAlign(CENTER);
      graphics.text("Q.head = " + str(idx + 1), x, y);
    graphics.endDraw();
  }
  y = margin_y + node_size + upper_size * 2 - 8;
  if (values[idx] == -1 && values[(idx + values.length - 1) % values.length] != -1) {
    graphics.beginDraw();
      graphics.fill(0, 0, 0);
      graphics.textFont(font, 22);
      graphics.textAlign(CENTER);
      graphics.text("Q.tail = " + str(idx + 1), x, y);
    graphics.endDraw();
  }
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  float w = values.length * node_size + margin_x * 2;
  float h = node_size + upper_size * 1.5 + margin_y * 2;
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
  for (int i = 0; i < values.length; ++i) {
    display(i);
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}