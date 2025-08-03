function toggleRewards() {
  const section = document.getElementById('rewards-section');
  section.style.display = (section.style.display === 'none') ? 'block' : 'none';
}


function toggleRewards() {
  const section = document.getElementById("rewards-section");
  section.classList.toggle("d-none");
}

document.addEventListener("DOMContentLoaded", function () {
  const donations = parseInt(document.getElementById("donation-amount")?.textContent || 0);
  const extraRewards = document.getElementById("extra-rewards");

  if (donations >= 1500) {
    const li = document.createElement("li");
    li.className = "list-group-item text-success fw-bold";
    li.textContent = "🎉 Premium Internship Certificate Unlocked!";
    extraRewards.appendChild(li);
  }
});


