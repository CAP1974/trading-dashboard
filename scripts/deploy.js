#!/usr/bin/env node
/**
 * deploy.js — git add . && git commit -m "update data" && git push origin main
 */

'use strict';

const { execSync } = require('child_process');
const path         = require('path');
const ROOT         = path.join(__dirname, '..');

function run(cmd) {
  execSync(cmd, { stdio: 'inherit', cwd: ROOT });
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
