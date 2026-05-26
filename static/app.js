let selectedFiles = [];

function handleFiles(files) {
    selectedFiles = Array.from(files);
    renderFileList();
}

function handleDrop(event) {
    event.preventDefault();
    document.getElementById('upload-box').classList.remove('drag-over');
    selectedFiles = Array.from(event.dataTransfer.files);
    renderFileList();
}

function renderFileList() {
    const list = document.getElementById('file-list');
    const btn = document.getElementById('analyze-btn');
    list.innerHTML = '';
    selectedFiles.forEach(file => {
        const item = document.createElement('div');
        item.className = 'file-item';
        item.innerHTML = `<div class="file-dot"></div><span>${file.name}</span>`;
        list.appendChild(item);
    });
    btn.style.display = selectedFiles.length > 0 ? 'inline-block' : 'none';
}

async function runAnalysis() {
    if (selectedFiles.length === 0) return;
    showLoading(true);
    const formData = new FormData();
    selectedFiles.forEach(file => formData.append('files', file));
    try {
        const res = await fetch('/analyze', { method: 'POST', body: formData });
        const data = await res.json();
        renderResults(data);
    } catch (e) {
        alert('Something went wrong. Please try again.');
    }
    showLoading(false);
}

async function runSample() {
    showLoading(true);
    try {
        const res = await fetch('/sample', { method: 'POST' });
        const data = await res.json();
        renderResults(data);
    } catch (e) {
        alert('Something went wrong. Please try again.');
    }
    showLoading(false);
}

function renderResults(data) {
    document.getElementById('results-section').style.display = 'block';

    const high = data.themes.filter(t => t.severity.toLowerCase() === 'high').length;
    document.getElementById('snapshot-grid').innerHTML = `
        <div class="snapshot-card"><div class="snapshot-number">${data.themes.length}</div><div class="snapshot-label">Themes identified</div></div>
        <div class="snapshot-card"><div class="snapshot-number">${data.pain_points.length}</div><div class="snapshot-label">Pain points</div></div>
        <div class="snapshot-card"><div class="snapshot-number">${data.user_needs.length}</div><div class="snapshot-label">User needs</div></div>
        <div class="snapshot-card"><div class="snapshot-number">${high}</div><div class="snapshot-label">High severity</div></div>
    `;

    document.getElementById('summary-text').textContent = data.summary;

    document.getElementById('pain-points-list').innerHTML = data.pain_points
        .map(p => `<li class="finding-item">${p}</li>`).join('');

    document.getElementById('user-needs-list').innerHTML = data.user_needs
        .map(n => `<li class="finding-item">${n}</li>`).join('');

    document.getElementById('themes-list').innerHTML = data.themes.map((t, i) => `
        <div class="theme-item">
            <div class="theme-header" onclick="toggleTheme(${i})">
                <span class="theme-name">${t.name}</span>
                <span class="severity-badge severity-${t.severity.toLowerCase()}">${t.severity.toUpperCase()}</span>
            </div>
            <div class="theme-body" id="theme-${i}">
                <p class="theme-desc">${t.description}</p>
                ${t.quotes.map(q => `<div class="quote">${q}</div>`).join('')}
            </div>
        </div>
    `).join('');

    document.getElementById('results-section').scrollIntoView({ behavior: 'smooth' });
}

function toggleTheme(i) {
    const body = document.getElementById(`theme-${i}`);
    body.classList.toggle('open');
}

function showLoading(show) {
    document.getElementById('loading-overlay').style.display = show ? 'flex' : 'none';
}