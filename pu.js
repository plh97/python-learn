const puppeteer = require('puppeteer');
const dely = ms => new Promise(res=> setTimeout(res,ms));

(async () => {
  let pageIndex = 133;
  const browser = await puppeteer.launch({
    // 想要代码运的好，还得首选金丝雀
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    // "executablePath": "C:/Users/33318/AppData/Local/Google/Chrome SxS/Application/chrome.exe",
    timeout: 0,
    // headless: false,
    slowMo: 1,
  });
  const page = await browser.newPage();
  await page.setViewport({
    width: 1600,
    height: 0,
  });
  console.log('设置窗口大小成功');
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);
  
  console.log(`去到follow第${pageIndex}页面成功`);

  const btns = await page.$('.text-bold.text-white.no-underline')
  btns.click()
  
  await page.waitFor('input[name=login]');
  await page.waitFor('input[name=password]');
  const name = await page.$('input[name=login]');
  const password = await page.$('input[name=password]');
  await name.type('pengliheng');
  await password.type('ewqewq123');
  console.log(`成功输入账号密码`);
  await page.keyboard.press('Enter');



  await page.waitFor('.UnderlineNav.user-profile-nav.js-sticky.top-0');

  // debug tools
  // await page.evaluate(() => {
  //   window.addEventListener('mousemove', (e) => {
  //     try {
  //       const div = document.createElement('div');
  //       div.style.width = '5px';
  //       div.style.height = '5px';
  //       div.style.borderRadius = '50%';
  //       div.style.backgroundColor = 'red';
  //       div.style.position = 'absolute';
  //       div.style.left = `${e.x + 5}px`;
  //       div.style.top = `${e.y + 5}px`;
  //       div.style.zIndex = '99999';
  //       document.body.appendChild(div);
  //     } catch (err) {
  //       console.error(err);
  //     }
  //   });
  // });
  
  // back to gitter
  await page.setViewport({
    width: 1000,
    height: 800,
  });
  
  console.log(`重新设置窗口大小`);

  
  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);

  console.log(`去到follow第${pageIndex}页面成功`);




  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);





  _btns = await page.$$('.btn.btn-sm.js-toggler-target')
  for (let i = 0; i < _btns.length; i++) {
    if(i>2 && i%2==0){
      console.log(`当前页面第${i}条，当前是第${pageIndex}页`);
      await dely(3000)
      await _btns[i] && _btns[i].click()
    }
  }
  await page.goto(`https://github.com/KevinHock?page=${pageIndex++}&tab=following`);



})()