function grade(score1, score2, score3) {
  let avg = (score1 + score2 + score3) / 3;

  if (avg > 90 && avg < 100) {
    console.log('A');
  } else if (avg > 70 && avg < 80) {
    console.log('B');
  } else if (avg > 50 && avg < 65) {
    console.log('C');
  } else if (avg > 25 && avg < 50) {
    console.log('D');
  } else if (avg < 25) {
    console.log('წადი ისწავლე და მერე მოდი');
  }
}