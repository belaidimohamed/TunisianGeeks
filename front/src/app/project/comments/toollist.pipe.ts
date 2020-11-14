import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'toollist'
})
export class ToollistPipe implements PipeTransform {

  transform(lines: any): string {

    let list: string = '';

    lines.forEach(line => {
      list += line.name + '\n';
    });

    return list;
  }

}
