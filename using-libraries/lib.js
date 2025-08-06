import {Application, MeshPlane, Assets} from 'pixi.js';

(async () => 
{
    const app = new Application();
    await app.init({ background: 'black', resizable: window });
    document.body.append(app.canvas);

    const texture = await Assets.load('https://pixi.js.com/assets/bg_grass.jpg');
    const plane = new MeshPlane({ texture, verticesX: 10, verticesY: 10});
    plane.x = 100;
    plane.y = 100;
    app.stage.addChild(plane);

    const { buffer } = plane.geometry.getAttribute('aPosition');

    let timer = 0;
    app.ticker.add(() =>
    {
        for (let i = 1; i < buffer.data.length; i+=2)
        {
            buffer.data[i] += Math.sin(timer / 10+1) * 0.5;
        }
        buffer.update();
        timer++;
});

});