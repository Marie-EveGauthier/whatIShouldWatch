<?php

namespace Tuto\TestBundle\Controller;

use Symfony\Component\Form\Extension\Core\Type\ChoiceType;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;
use AppBundle\Entity\RedditAuthor;
use AppBundle\Entity\RedditPost;
use Doctrine\ORM\EntityManagerInterface;
use Symfony\Component\HttpFoundation\Response;

class DefaultController extends Controller {

    public function testAction() {
        $film = $this->getDoctrine()
                ->getRepository('TutoTestBundle:films')
                ->findall();

        return $this->render('TutoTestBundle:Default:filmview.html.twig', array(
                    'film' => $film));
    }

    public function filtersAction() {

        return $this->render('TutoTestBundle:Default:filters.html.twig');
    }

    public function resultatAction(Request $request) {
// for the request DBL
        $em = $this->getDoctrine()->getManager();
        // to get the value of the checkbox
        $checked_woman = $this->get('request')->request->get('woman_name');
        $checked_bechdel = $this->get('request')->request->get('button_bechdel');
        if (($checked_woman) && ($checked_bechdel)) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.dialogueWomen > p.dialogueMen and p.bechdel>0'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
        } else if ($checked_woman) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.dialogueWomen > p.dialogueMen'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
        } else if ($checked_bechdel) {
            $query = $em->createQuery(
                    'SELECT p
    FROM TutoTestBundle:films p
    WHERE p.bechdel > 0'
            );

            $products = $query->getResult();
            return $this->render('TutoTestBundle:Default:resultat.html.twig', array(
                        'products' => $products));
//..
        } else {
            return $this->render('TutoTestBundle:Default:filters.html.twig')
            ;
        }
    }

}
