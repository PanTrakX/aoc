const fs = require("fs");

fs.readFile("../input.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  // Part 1
  let a = data.split("\n\n").map((item) =>
    item
      .replace(/^\s+|\s+$/g, "")
      .split("\n")
      .reduce((acc, cur) => {
        return acc + Number.parseInt(cur, 10);
      }, 0)
  );
  console.log(Math.max(...a));

  // Part 2
  let b = a;
  let s = 0;
  for (i = 0; i < 3; i++) {
    let max = Math.max(...b);
    s += max;
    b.splice(b.indexOf(max), 1);
  }
  console.log(s);

  return 0;
});
