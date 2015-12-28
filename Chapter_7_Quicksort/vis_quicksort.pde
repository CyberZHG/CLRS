PGraphics graphics;
PFont font;

String[] names  = new String[] {"", "9", "5", "8", "7", "4", "13", "19", "12", "21", "2", "6", "11"};
String[] uppers = new String[] {" ", "p", " ", " ", " ", "i", " ", " ", " ", "j", " ", " ", "r"};
String[] types  = new String[] {" ", "l", "l", "l", "l", "l", "r", "r", "r", "d", "d", "d", "p"};
String save_name = "7.1-1_9.png";

float node_size = 50;
float upper_size = 35;
float margin_x = 40;
float margin_y = 30;

void display(int idx) {
  float x = margin_x + idx * node_size;
  float y = margin_y + upper_size;
  graphics.beginDraw();
    graphics.strokeWeight(2);
    if (types[idx] == "d") {
      graphics.stroke(120, 120, 120);
      graphics.fill(165, 165, 165);
    } else if (types[idx] == "p") {
      graphics.stroke(174, 90, 33);
      graphics.fill(237, 125, 49);
    } else if (types[idx] == "l") {
      graphics.stroke(80, 126, 50);
      graphics.fill(112, 173, 71);
    } else if (types[idx] == "r") {
      graphics.stroke(65, 113, 156);
      graphics.fill(91, 155, 213);
    } else {
      graphics.stroke(255, 255, 255);
      graphics.fill(255, 255, 255);
    }
    graphics.rect(x + 0.5, y + 0.5, node_size - 1, node_size - 1);
  graphics.endDraw();
  x += node_size * 0.5;
  y += node_size * 0.5 + 8;
  graphics.beginDraw();
    graphics.fill(250, 250, 250);
    graphics.textFont(font, 22);
    graphics.textAlign(CENTER);
    graphics.text(names[idx], x, y);
  graphics.endDraw();
  y = margin_y + upper_size * 0.5 + 8;
  graphics.beginDraw();
    graphics.fill(0, 0, 0);
    graphics.textFont(font, 22);
    graphics.textAlign(CENTER);
    graphics.text(uppers[idx], x, y);
  graphics.endDraw();
}

void setup() {
  size(800, 600);
  smooth(8);
  noLoop();
  float w = names.length * node_size + margin_x * 2;
  float h = node_size + upper_size + margin_y * 2;
  graphics = createGraphics(int(w), int(h), JAVA2D);
  graphics.smooth(8);
  font = createFont("Arial", 22, true);
}

void draw() {
  background(255);
  graphics.beginDraw();
    graphics.fill(250, 250, 250);
    graphics.textFont(font, 18);
    graphics.textAlign(LEFT);
    graphics.text("https://github.com/CyberZHG/", 10, 23);
  graphics.endDraw();
  for (int i = 0; i < names.length; ++i) {
    display(i);
  }
  image(graphics, 0, 0);
  graphics.save(save_name);
}