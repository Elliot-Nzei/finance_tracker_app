function navigateTo(page) {
  fetch(`pages/${page}.html`)
    .then((res) => res.text())
    .then((html) => {
      document.getElementById('app').innerHTML = html;
      if (page === 'dashboard') loadDashboard();
      if (page === 'settings') loadSettings();
    });
}

function logout() {
  localStorage.clear();
  navigateTo('login');
}

function uploadStatement() {
  const file = document.getElementById('bank-statement').files[0];
  const formData = new FormData();
  formData.append('file', file);

  fetch('/api/finance/analyze', {
    method: 'POST',
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      const list = document.getElementById('summary-list');
      list.innerHTML = '';
      for (let item of data.summary) {
        const li = document.createElement('li');
        li.textContent = item;
        list.appendChild(li);
      }
    });
}

function setBudget() {
  const budget = document.getElementById('budget').value;
  fetch('/api/finance/budget', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ amount: budget }),
  });
}

function loadDashboard() {
  const user = JSON.parse(localStorage.getItem('user'));
  document.getElementById('welcome-user').textContent = `Welcome, ${user.name}`;
}

function loadSettings() {
  // Future implementation
}

document.addEventListener('DOMContentLoaded', () => {
  const user = localStorage.getItem('user');
  if (!user) navigateTo('login');
  else navigateTo('dashboard');
});
