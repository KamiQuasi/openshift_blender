import { Application, Router, HttpError, Status, send } from "https://deno.land/x/oak/mod.ts";
import { viewEngine, engineFactory, adapterFactory} from 'https://deno.land/x/view_engine/mod.ts';
import { upload } from 'https://deno.land/x/upload_middleware_for_oak_framework/mod.ts';

const ejsEngine = engineFactory.getEjsEngine();
const oakAdapter = adapterFactory.getOakAdapter();

const app = new Application();
const router = new Router();

// Error Handling
app.use(async (context, next) => {
  try {
    await next();
  } catch (e) {
    if (e instanceof HttpError) {
      context.response.status = e.status as any;
      if (e.expose) {
        context.response.body = `<!doctype html><html><body><h1>${e.status} - ${e.message}</h1></body></html>`;
      } else {
        context.response.body = `<!doctype html><html><body><h1>${e.status} - ${Status[e.status]}</h1></body></html>`;
      }
    } else if (e instanceof Error) {
      context.response.status = 500;
      context.response.body = `<!doctype html><html><body><h1>500 - Internal Server Error</h1></body></html>`;
      console.log("Unhandled Error:", e.message);
      console.log(e.stack);
    }
  }
});

app.use(viewEngine(oakAdapter, ejsEngine));

router
  .get('/', ctx => {
    ctx.render('index.ejs')
  })
  .post('/upload', upload('uploads'), async(ctx:any, next:any) => {
    const file = ctx.uploadedFiles;
    console.log(file);
    const p = Deno.run({
      cmd: ["blender", "-b", "-o images/image.png", ""]
    });
    const {code} = await p.status();
    if (code === 0) {
      const rawOutput = await p.output();
      await Deno.stdout.write(rawOutput);
    } else {
      const rawError = await p.stderrOutput();
      const errorString = new TextDecoder().decode(rawError);
      console.log(errorString);
    }
    ctx.response.redirect('/view');
  });

app.use(router.routes());
app.use(router.allowedMethods());

app.addEventListener('listen', ({hostname, port}) => {
  console.log(`Serving ${Deno.cwd()}`);
  console.log(`Start listening on ${hostname}:${port}`);
})

await app.listen({hostname: "0.0.0.0", port: 8000 });
