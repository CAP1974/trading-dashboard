#!/usr/bin/env node
/**
 * deploy.js — copia dashboard/data.js → ./data.js, depois git add/commit/push
 */

'use strict';

const { execSync } = require('child_process');
const fs   = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');

function run(cmd) {
  execSync(cmd, { stdio: 'inherit', cwd: ROOT });
}

// Copia dashboard/data.js para raiz (se existir)
const src = path.join(ROOT, 'dashboard', 'data.js');
const dst = path.join(ROOT, 'data.js');
if (fs.existsSync(src)) {
  fs.copyFileSync(src, dst);
  console.log('Copiado dashboard/data.js → ./data.js');
}

try {
  run('git add .');
  // Only commit if there are staged changes
  const status = execSync('git status --porcelain', { cwd: ROOT }).toString().trim();
  if (!status) {
    console.log('Nothing to commit — working tree clean.');
  } else {
    run('git commit -m "update data"');
    console.log('Committed.');
  }
  run('git push origin main');
  console.log('Pushed to origin/main.');
} catch (e) {
  console.error('Deploy failed:', e.message);
  process.exit(1);
}
